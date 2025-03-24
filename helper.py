def save_results_to_file(results, output_file="experiment_results.txt"):
    with open(output_file, "w") as f:
        f.write(results)
    print(f"Results saved to {output_file}")

