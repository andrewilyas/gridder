tmux new-session -d -s sess-0 -n 0
tmux send-keys -t sess-0:0 "source ~/.exp_rc" Enter
tmux new-session -d -s sess-1 -n 0
tmux send-keys -t sess-1:0 "source ~/.exp_rc" Enter
tmux new-session -d -s sess-2 -n 0
tmux send-keys -t sess-2:0 "source ~/.exp_rc" Enter
tmux new-session -d -s sess-3 -n 0
tmux send-keys -t sess-3:0 "source ~/.exp_rc" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job0-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job1-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job2-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-3:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job3-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job4-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job5-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job6-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-3:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job7-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job8-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job9-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job10-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-3:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job11-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job12-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job13-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job14-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-3:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job15-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job16-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job17-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job18-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-3:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job19-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job20-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job21-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job22-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-3:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job23-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-0:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job24-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-1:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job25-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter

tmux send-keys -t sess-2:0 "gridder-run --num-gpus 2 --gpu-lim 1              --config /tmp/dummy/job26-1301bbb2-0f85-44f3-98e1-f2372111480b.json --proj-url /data/theory/robustopt/andrew/gridder/example             --main-file to_run.py --clone-type fs" Enter
