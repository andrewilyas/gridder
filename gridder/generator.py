from .utils import dict_product
from uuid import uuid4
import pandas as pd
import json
import os

TMUX_INIT = \
"""tmux new-session -d -s {0} -n 0
tmux send-keys -t {0}:0 "source ~/.exp_rc" Enter
"""

TMUX_JOB = """
tmux send-keys -t {0}:0 "{1}" Enter
"""

RUNNER = "gridder-run --num-gpus {gpus_per_job} --gpu-lim {max_jobs_per_gpu}  \
        --config {config} --proj-url {proj_url} --main-file {path_to_main}"

RUNNER_KEYS = ["gpus_per_job", "max_jobs_per_gpu", "config", 
                    "proj_url", "path_to_main"]

DELETE_ALL_JOBS = """
rm -f {0}
"""

PATH_KEY = "_experiment_path"

def consolidate_experiment(exp_csv, N, runner_args, prefix="sess"):
    """
    Consolidates a set of generated json files into a run and cleanup script
    that can be run.
    """
    exp_df = pd.read_csv(exp_csv)
    job_str = ""
    cleanup_str = ""

    # Start a worker (tmux session)
    for worker in range(min(N, len(exp_df))):
        job_str += TMUX_INIT.format(f"{prefix}-{worker}")

    # Go through the experiments one by one
    for i, exp_path in enumerate(exp_df[PATH_KEY]):
        runner_args['config'] = exp_path
        sess_name = f"{prefix}-{i % N}"
        runner_str = RUNNER.format(**runner_args)
        job_str += TMUX_JOB.format(sess_name, runner_str)
        cleanup_str += TMUX_JOB.format(sess_name, f"rm -f {exp_path}")
    return job_str, cleanup_str

def generate_experiments(base, params_to_vary, exp_dir, rules=[], sort_by=None):
    '''
    Given a function to test, a base set of hyperparameters to vary, 
    we generate the appropriate config files and scripts to run the 
    tests and collect the results.

    The results will be collected over a grid of hyperparameters given
    by a cartesian product, but filtered by a set of specified rules.

    Args:
        base (Dict[String:Any]), default values for all necessary hyperparams
        params (Dict[String:List[Any]]), params and values to be gridded over
        exp_dir (str) : path to the directory where the experiments are to be
            saved
    '''
    params_df_cols = set(base.keys()) | set(params_to_vary.keys()) | {PATH_KEY}
    params_df = pd.DataFrame(columns=list(params_df_cols))

    all_test_params = dict_product(params_to_vary)
    if sort_by:
        if not isinstance(sort_by, list):
            sort_by = [sort_by]
        for i in reversed(sort_by):
            all_test_params = sorted(all_test_params, key=lambda d:-d[i])

    filt_params = all_test_params
    exp_uid = str(uuid4())

    for rule in rules:
        filt_params = list(filter(rule, filt_params))

    for i, fd in enumerate(filt_params):
        job_name = "job%d-%s" % (i, exp_uid)
        new_job = dict(base, **fd)
        fname = os.path.join(exp_dir, "%s.json" % (job_name,))
        new_job[PATH_KEY] = fname
        params_df.loc[i,list(new_job.keys())] = list(new_job.values())
        json.dump(new_job, open(fname, "w"))

    csv_path = os.path.join(exp_dir, "all_experiments.csv")
    params_df.to_csv(csv_path)
    return csv_path
