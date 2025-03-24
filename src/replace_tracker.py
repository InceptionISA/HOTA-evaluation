import os
import glob
import shutil
import re
from .helper import reverse_submission

def extract_number(filename):
    """Extracts the numeric part from the filename (e.g., 3 from 'submission_3_lorem.txt')."""
    match = re.search(r"submission_(\d+)", filename)
    return int(match.group(1)) if match else -1

def get_latest_tracker_file(trackfiles_dir):
    """Finds the latest tracker file in the trackfiles directory based on the numeric part of the filename."""
    files = glob.glob(os.path.join(trackfiles_dir, "submission_*"))
    if not files:
        raise FileNotFoundError(f"No files found in {trackfiles_dir}")
    return max(files, key=lambda f: extract_number(os.path.basename(f)))

def extract_metadata_from_filename(filename):
    """Extracts metadata from the filename (e.g., 'metadata' from 'submission_4_metadata.txt')."""
    match = re.search(r"submission_\d+_(.+)\.\w+", filename)
    return match.group(1) if match else None

def extract_filename_without_extension(path):
    """Extracts the filename without its extension."""
    return os.path.splitext(os.path.basename(path))[0]

def replace_tracker_file():
    """Handles replacing the tracker file with the latest submission, converting CSV files if necessary."""
    trackfiles_dir = "trackfiles"
    hota_tracker_file = "HOTA-metrics/data/trackers/mot_challenge/MOT20-train/my_tracker/data/MOT20-01.txt"

    latest_file_path = get_latest_tracker_file(trackfiles_dir)
    latest_file_name = os.path.basename(latest_file_path)
    file_ext = os.path.splitext(latest_file_name)[1]

    print(f"Latest tracker file found: {latest_file_name}")

    # Convert CSV files to TXT if necessary
    if file_ext == ".csv":
        print("CSV file detected. Converting to TXT...")
        converted_file_path = os.path.join(trackfiles_dir, f"{extract_filename_without_extension(latest_file_name)}_converted.txt")
        latest_file_path = reverse_submission(latest_file_path, output_path=converted_file_path)
        latest_file_name = os.path.basename(latest_file_path)
        print(f"Converted to TXT: {latest_file_name}")

    metadata = extract_metadata_from_filename(latest_file_name)
    print(f"Metadata from filename: {metadata}" if metadata else "No metadata found in filename.")

    # Replace the existing tracker file
    if os.path.exists(hota_tracker_file):
        os.remove(hota_tracker_file)
        print(f"Removed existing tracker file: {hota_tracker_file}")

    shutil.copy(latest_file_path, hota_tracker_file)
    print(f"Copied {latest_file_name} to {hota_tracker_file} (renamed to MOT20-01.txt)")

    return latest_file_name, metadata
