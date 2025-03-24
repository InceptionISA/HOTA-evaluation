import os

def get_evaluation_command():
    # Define paths
    base_dir = "HOTA-metrics"
    benchmark = "MOT20"
    tracker_name = "my_tracker"

    eval_script = os.path.join(base_dir, "scripts", "run_mot_challenge.py")

    command = (
        f"python {eval_script} "
        f"--BENCHMARK {benchmark} "
        f"--TRACKERS_TO_EVAL {tracker_name} "
        f"--METRICS HOTA "
        f"--USE_PARALLEL False "
        f"--NUM_PARALLEL_CORES 1"
    )

    return command
