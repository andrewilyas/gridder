from .generator import generate_experiments, PATH_KEY, consolidate_experiment
import shutil
import os
import tempfile
import subprocess
import json
import argparse
from importlib.util import spec_from_file_location, module_from_spec
import uuid

def main():
    parser = argparse.ArgumentParser(description='Generate experiments to be run.')
    parser.add_argument('-b', '--base-config', type=str)
    parser.add_argument('-o', '--out-dir', type=str, required=True)
    parser.add_argument('-e', '--experiment-config', type=str, required=True)
    parser.add_argument('-r', '--run', action='store_true')
    parser.add_argument('-p', '--session-prefix', type=str, default='sess')
    args = parser.parse_args()

    spec = spec_from_file_location("config", args.experiment_config)
    config = module_from_spec(spec)
    spec.loader.exec_module(config)

    if False:
        raise ValueError("experiment-config-path should be a pointer to a python file \
                                with NUM_SESSIONS, CMD_MAKER, RULES, and PARAMS defined. \
                                To generate an example experimental config file with comments, \
                                run 'gridder-gen-config'.")

    base = json.load(open(args.base_config)) if args.base_config else {}
    base['out_dir'] = args.out_dir

    tmp_path = f"/tmp/{str(uuid.uuid4())}"
    if config.LOCATION_IS_GIT:
        Repo.clone_from(config.PROJECT_LOCATION, tmp_path)
    else:
        shutil.copytree(config.PROJECT_LOCATION, tmp_path)

    csv_path = generate_experiments(base, config.PARAMS, args.out_dir, rules=config.RULES)
    runner_args = {
        'gpus_per_job': config.GPUS_PER_JOB, 
        'max_jobs_per_gpu': config.MAX_JOBS_PER_GPU,
        'proj_url': tmp_path,
        'path_to_main': config.PATH_TO_MAIN,
    }
    job_str, cleanup_str = consolidate_experiment(csv_path, config.NUM_SESSIONS,
                                runner_args, prefix=args.session_prefix)

    open("run.sh", "w").write(job_str)
    open("cleanup.sh", "w").write(cleanup_str)

if  __name__=="__main__":
    main()
