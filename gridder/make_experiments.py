from .generator import generate_experiments, PATH_KEY, consolidate_experiment
import os
import tempfile
import subprocess
import json
import argparse
from importlib.util import spec_from_file_location, module_from_spec

def main():
    parser = argparse.ArgumentParser(description='Generate experiments to be run.')
    parser.add_argument('-b', '--base-config-path', type=str)
    parser.add_argument('-o', '--out-dir', type=str, required=True)
    parser.add_argument('-e', '--experiment-config-path', type=str, required=True)
    parser.add_argument('-r', '--run', action='store_true')
    parser.add_argument('-p', '--session-prefix', type=str, default='sess')
    args = parser.parse_args()

    spec = spec_from_file_location("config", args.experiment_config_path)
    config = module_from_spec(spec)
    spec.loader.exec_module(config)

    if False:
        raise ValueError("experiment-config-path should be a pointer to a python file \
                                with NUM_SESSIONS, CMD_MAKER, RULES, and PARAMS defined. \
                                To generate an example experimental config file with comments, \
                                run 'gridder-gen-config'.")

    if args.base_config_path:
        base = json.load(open(args.base_config_path))
    else:
        base = {}
    base['out_dir'] = args.out_dir

    gen_kwargs = {
        'rules':config.RULES
    }

    csv_path = generate_experiments(base, config.PARAMS, args.out_dir, **gen_kwargs)
    runner_args = {
        'gpus_per_job': config.GPUS_PER_JOB, 
        'max_jobs_per_gpu': config.MAX_JOBS_PER_GPU,
        'proj_url': config.PROJECT_LOCATION,
        'path_to_main': config.PATH_TO_MAIN,
        'use_git': ('git' if config.LOCATION_IS_GIT else 'fs')
    }
    job_str, cleanup_str = consolidate_experiment(csv_path, config.NUM_SESSIONS,
                                runner_args, prefix=args.session_prefix)

    open("run.sh", "w").write(job_str)
    open("cleanup.sh", "w").write(cleanup_str)

if  __name__=="__main__":
    main()
