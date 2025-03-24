import os
import glob
import shutil
import re

def extract_number(filename):
    """
    Extracts the numeric part from the filename (e.g., 3 from 'submission_3_lorem.txt').
    """
    match = re.search(r"submission_(\d+)", filename)
    if match:
        return int(match.group(1))
    return -1  # Return -1 if no number is found

def get_latest_tracker_file(trackfiles_dir):
    """
    Finds the latest tracker file in the trackfiles directory based on the numeric part of the filename.
    """
    # Get all files in the trackfiles directory
    files = glob.glob(os.path.join(trackfiles_dir, "submission_*"))
    
    if not files:
        raise FileNotFoundError(f"No files found in {trackfiles_dir}")
    
    # Find the file with the highest numeric part in the filename
    latest_file = max(files, key=lambda f: extract_number(os.path.basename(f)))
    return latest_file

def extract_metadata_from_filename(filename):
    """
    Extracts the metadata from the filename (e.g., 'metadata' from 'submission_4_metadata.txt').
    """
    # Extract the part after the number and underscore
    match = re.search(r"submission_\d+_(.+)\.txt", filename)
    if match:
        return match.group(1)
    return None  # Return None if no metadata is found

def extract_filename_from_path(path):
    return os.path.splitext(os.path.basename(path))[0]

def replace_tracker_file():
    """
    Replaces the tracker file in the HOTA directory with the latest file from trackfiles,
    renames it to MOT20-01.txt, and returns the filename and metadata.
    """
    # Define paths
    trackfiles_dir = "trackfiles"  # Directory containing tracker files
    hota_tracker_file = "HOTA-metrics/data/trackers/mot_challenge/MOT20-train/my_tracker/data/MOT20-01.txt"  # Path to replace
    
    # Get the latest tracker file
    latest_file_path = get_latest_tracker_file(trackfiles_dir)
    latest_file_name = extract_filename_from_path(latest_file_path)
    print(f"Latest tracker file found: {latest_file_name}")
    
    # Extract the metadata from the filename
    metadata = extract_metadata_from_filename(latest_file_name)
    if metadata:
        print(f"Metadata from filename: {metadata}")
    else:
        print("No metadata found in filename.")
    
    # Remove the existing tracker file if it exists
    if os.path.exists(hota_tracker_file):
        os.remove(hota_tracker_file)
        print(f"Removed existing tracker file: {hota_tracker_file}")
    
    # Copy the latest tracker file to the HOTA directory and rename it
    shutil.copy(latest_file_path, hota_tracker_file)
    print(f"Copied {latest_file_name} to {hota_tracker_file} (renamed to MOT20-01.txt)")
    
    return latest_file_name, metadata

