import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("results/data_preprocessed.csv")

X = df[['pca_1', 'pca_2']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster_label'] = kmeans.fit_predict(X)

cols_to_save = [col for col in ['Customer ID', 'cluster_label'] if col in df.columns]
cluster_output = df[cols_to_save]

cluster_output.to_csv("results/clusters.txt", sep='\t', index=False)

df.to_csv("results/data_clustered.csv", index=False) 
