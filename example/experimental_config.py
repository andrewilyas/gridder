from gridder.generator import PATH_KEY

NUM_SESSIONS = 4
PARAMS = {
    "x": [1, 2, 3],
    "y": [4, 5, 6],
    "z": [7, 8, 9]
}

GPUS_PER_JOB = 2
MAX_JOBS_PER_GPU = 1
PROJECT_LOCATION = '/data/theory/robustopt/andrew/gridder/example'
PATH_TO_MAIN = 'to_run.py'
LOCATION_IS_GIT = False

RULES = []

