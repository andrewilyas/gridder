import GPUtil
from cox import utils
from git import Repo
import json
import os
import time
import fcntl
import uuid
import argparse
import shutil
from importlib.util import spec_from_file_location, module_from_spec

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-gpus', type=int)
    parser.add_argument('--gpu-lim', type=int)
    parser.add_argument('--config', type=str)
    parser.add_argument('--proj-url', type=str)
    parser.add_argument('--main-file', type=str)
    args = parser.parse_args()

    CUDA_KEY = 'CUDA_VISIBLE_DEVICES'
    os.environ[CUDA_KEY] = ''

    # Only one process can select GPUs at a time, otherwise we get ugly stuff
    print("Waiting to acquire the global lock...")
    while True:
        try:
            big_lock_name = f'/tmp/acquiring_gpu_lock'
            big_lock = open(big_lock_name, 'w')
            fcntl.flock(big_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except IOError:
            time.sleep(1)
    print("Acquired the global lock")

    to_exclude = []
    locks = []
    while True:
        ids = GPUtil.getAvailable(order = 'first', limit = args.num_gpus, maxLoad = 0.5,
                maxMemory = 1/args.gpu_lim - 0.05, excludeID=to_exclude)
        if len(ids) < args.num_gpus: 
            print(f"Waiting for GPUs ({len(ids)} available, {args.num_gpus} needed)")
            time.sleep(1)
            continue
        
        print(f"Found GPUs {ids}, trying to claim...")
        for gpu in ids:
            for i in range(args.gpu_lim):
                lock_name = f"/tmp/{gpu}_{i}"
                try:
                    gpu_lock = open(lock_name, 'w')
                    fcntl.flock(gpu_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    locks.append((gpu_lock, lock_name))
                    os.environ[CUDA_KEY] = f"{gpu},{os.environ[CUDA_KEY]}"
                    break
                except:
                    pass
            else:
                # Can't get the lock for one of the GPUs, start over
                to_exclude.append(gpu)
                print("Lock taken, clearing locks and trying again")
                for fh, fname in locks:
                    del fh
                    os.remove(fname)
                break
        else:
            print(f"Successfully acquired {ids}")
            break

    # Release the lock on looking for GPUs
    del big_lock
    os.remove(big_lock_name)


    tmp_path = f"/tmp/{str(uuid.uuid4())}"
    shutil.copytree(args.proj_url, tmp_path)
    
    exp_path = os.path.join(tmp_path, args.main_file)
    spec = spec_from_file_location("experiment", exp_path)
    experiment = module_from_spec(spec)
    spec.loader.exec_module(experiment)

    params = utils.Parameters(json.load(open(args.config)))
    experiment.main(params)
    
    print("Cleaning up (removing locks and deleting repos)")
    for fh, fname in locks:
        os.remove(fname)
    shutil.rmtree(tmp_path)

if __name__ == '__main__':
    main()
