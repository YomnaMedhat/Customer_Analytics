import pandas as pd
import sys
import os
import subprocess

input_path = sys.argv[1]
df = pd.read_csv(input_path)

os.makedirs("results", exist_ok=True)

# Insight 1
avg_spend = df['Monthly Charge'].mean()
with open("results/insight1.txt", "w") as f:
    f.write(f"Average Monthly Charge: {avg_spend}\n")

# Insight 2
avg_tenure = df['Tenure in Months'].mean()
with open("results/insight2.txt", "w") as f:
    f.write(f"Average Tenure: {avg_tenure}\n")

# Insight 3
churn_rate = df['Churn Score'].mean()
with open("results/insight3.txt", "w") as f:
    f.write(f"Average Churn Score: {churn_rate}\n")

# Call next
subprocess.run(["python", "visualize.py", input_path])