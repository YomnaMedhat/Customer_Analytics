import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import subprocess

input_path = sys.argv[1]
df = pd.read_csv(input_path)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

# Histogram
plt.subplot(2, 2, 1)
sns.histplot(df['Monthly Charge'], kde=True)
plt.title('Monthly Charge Distribution')

# Heatmap
plt.subplot(2, 2, 2)
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr)

# PCA Scatter
plt.subplot(2, 2, 3)
sns.scatterplot(data=df, x='pca_1', y='pca_2')

plt.tight_layout()
plt.savefig("results/summary_plot.png")

subprocess.run(["python", "cluster.py", input_path])