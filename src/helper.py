import pandas as pd
import ast  # For safely evaluating string representations of lists

def save_results_to_file(results, output_file="experiment_results.txt"):
    with open(output_file, "w") as f:
        f.write(results)
    print(f"Results saved to {output_file}")




def reverse_submission(csv_path, output_path="tracking_results.txt"):

    df = pd.read_csv(csv_path)
    
    tracking_results = []
    
    for _, row in df.iterrows():
        frame = row["Frame"]
        objects = ast.literal_eval(row["Objects"])  # Convert string representation of list to actual list
        
        # Iterate over each object in the frame
        for obj in objects:
            tracked_id = obj["tracked_id"]
            x = obj["x"]
            y = obj["y"]
            w = obj["w"]
            h = obj["h"]
            confidence = obj["confidence"]
            
            # Append the data in the original format
            tracking_results.append(f"{frame},{tracked_id},{x},{y},{w},{h},{confidence},-1,-1,-1")
    
    # Write the tracking results to a TXT file
    with open(output_path, "w") as f:
        for line in tracking_results:
            f.write(line + "\n")
    
    print(f"Tracking results saved as {output_path}")

    return output_path