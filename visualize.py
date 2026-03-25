import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("results/data_clustered.csv")

sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# PLOT 1: HISTOGRAM (Distribution of Monthly Charges) 
plt.subplot(2, 2, 1)
sns.histplot(df['Monthly Charge'], kde=True, color='skyblue')
plt.title('Distribution of Monthly Charges')

# PLOT 2: HEATMAP (Correlation of numeric features) 
plt.subplot(2, 2, 2)
numeric_cols = df.select_dtypes(include=['number']).columns
corr = df[numeric_cols].corr()
sns.heatmap(corr, cmap='coolwarm', annot=False)
plt.title('Feature Correlation Heatmap')

# PLOT 3: SCATTER PLOT (The PCA Clusters) 
plt.subplot(2, 2, 3)
sns.scatterplot(data=df, x='pca_1', y='pca_2', hue='cluster_label', palette='viridis')
plt.title('Customer Clusters (PCA Space)')

# PLOT 4: BAR CHART (Tenure Bins vs Clusters) 
plt.subplot(2, 2, 4)
sns.countplot(data=df, x='cluster_label', hue='tenure_group')
plt.title('Tenure Bins per Cluster')

plt.tight_layout()
plt.savefig("results/analysis_results.png") 
plt.show()

print("Visualization complete! Check 'analysis_results.png' for your report.")