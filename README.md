# HOTA Evaluation Toolkit

This toolkit evaluates tracking performance using the HOTA metrics.

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/HOTA-evaluation.git
   cd HOTA-evaluation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Directory Structure

Place your files in these paths:

```
HOTA-evaluation/
├── trackfiles/                  # Put your tracker files here (e.g., submission_*.txt)
├── HOTA-metrics/
│   └── data/
│       ├── gt/                  # Ground truth data
│       └── trackers/            # Processed tracker files will be placed here
```

## Running the Evaluation

1. **Add your tracking files**:

   - Place your tracking files in `trackfiles/` directory
   - Files should be named like `submission_<number>_<metadata>.txt`

2. **Run the evaluation**:
   ```bash
   python -m main
   ```

## Output

Results will be:

- Saved in `experiments/` directory (named after metadata)
- Printed to console with HOTA metrics

## Example

For a file named `submission_1_test.txt`:

```bash
python -m main
```

Will create:

```
experiments/
└── test.txt    # Results file
```

## Requirements

- Python 3.6+
- pandas
- numpy
