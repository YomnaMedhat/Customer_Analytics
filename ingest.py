import sys
import pandas as pd
import subprocess


if len(sys.argv) < 2:
    print("Usage: python ingest.py <telco_customer_churn.csv>")
    sys.exit(1)

dataset_path = sys.argv[1]

df = pd.read_csv(dataset_path)

output_path = "data_raw.csv"
df.to_csv(output_path, index=False)

subprocess.run(["python", "preprocess.py", output_path])