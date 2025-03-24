import os

def create_hota_structure(base_dir="HOTA-metrics", benchmark="MOT20-train", sequences=["MOT20-01"], tracker_name="my_tracker"):
    # Define paths
    data_dir = os.path.join(base_dir, "data")
    gt_dir = os.path.join(data_dir, "gt", "mot_challenge")
    trackers_dir = os.path.join(data_dir, "trackers", "mot_challenge", benchmark, tracker_name, "data")  # Updated tracker path
    seqmap_dir = os.path.join(data_dir, "gt", "mot_challenge", "seqmaps")
    
    # Create directories
    os.makedirs(trackers_dir, exist_ok=True)  # Tracker data folder
    os.makedirs(seqmap_dir, exist_ok=True)  # Seqmaps folder
    
    # Create sequence folders inside the benchmark folder (without the 'gt' subfolder)
    for seq in sequences:
        os.makedirs(os.path.join(gt_dir, benchmark, seq), exist_ok=True)  # Sequence folder only
    
    # Create MOT20-train.txt in seqmaps
    seqmap_file = os.path.join(seqmap_dir, f"{benchmark}.txt")
    with open(seqmap_file, "w") as f:
        f.write("name\n")  # First line should be "name"
        for seq in sequences:
            f.write(f"{seq}\n")
    
    print("HOTA directory structure created successfully.")
    print(f"GT Folder: {os.path.join(gt_dir, benchmark)}")
    print(f"Tracker Folder: {trackers_dir}")
    print(f"Seqmap Folder: {seqmap_dir}")

# Run the function
create_hota_structure()