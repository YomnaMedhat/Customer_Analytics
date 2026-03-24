import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python ingest.py <telco_customer_churn.csv>")
    sys.exit(1)

dataset_path = sys.argv[1]

df = pd.read_csv(dataset_path)

df.to_csv("data_raw.csv", index=False)