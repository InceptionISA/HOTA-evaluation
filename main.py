import os
import subprocess
from src.create_command import get_evaluation_command
from src.replace_tracker import replace_tracker_file
from src.helper import save_results_to_file
from src.helper import reverse_submission

def main():

    filename,metadata = replace_tracker_file()


    command = get_evaluation_command()

    print("Running evaluation...")

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print("Evaluation completed successfully.")

        save_results_to_file(result.stdout, f'expermetns/experiment_results_of_{filename}')
    else:
        print("Evaluation failed with the following error:")
        print(result.stderr)



if __name__ == "__main__":
    main()


