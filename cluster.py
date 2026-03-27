import pandas as pd
from sklearn.cluster import KMeans
import sys

input_path = sys.argv[1]
df = pd.read_csv(input_path)

X = df[['pca_1', 'pca_2']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

counts = df['cluster'].value_counts()

with open("results/clusters.txt", "w") as f:
    for cluster, count in counts.items():
        f.write(f"Cluster {cluster}: {count} samples\n")

df.to_csv("results/data_clustered.csv", index=False)