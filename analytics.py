import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(current_dir, 'results')

if not os.path.exists(results_dir):
    os.makedirs(results_dir)

try:
    df = pd.read_csv(os.path.join(current_dir, "data_clustered.csv"))
    
    report_path = os.path.join(results_dir, "analytics_insights.txt")
    
    with open(report_path, "w") as f:
        f.write("CLUSTER ANALYTICS REPORT\n")
        f.write("="*35 + "\n\n")

        # Insight 1: Spending
        avg_spend = df.groupby('cluster_label')['Monthly Charge'].mean()
        f.write(f"INSIGHT 1: Average Monthly Charge per Cluster\n{avg_spend}\n\n")

        # Insight 2: Loyalty (The Bins!)
        risk_profile = df.groupby(['cluster_label', 'tenure_group']).size().unstack(fill_value=0)
        f.write(f"INSIGHT 2: Loyalty Distribution per Cluster\n{risk_profile}\n\n")

        # Insight 3: Usage
        avg_usage = df.groupby('cluster_label')['Avg Monthly GB Download'].mean()
        f.write(f"INSIGHT 3: Average Data Usage (GB) per Cluster\n{avg_usage}\n")

except FileNotFoundError:
    print("Error: 'data_clustered.csv' not found. Run cluster.py first!")