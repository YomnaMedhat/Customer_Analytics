import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("results/data_preprocessed.csv")

X = df[['pca_1', 'pca_2']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster_label'] = kmeans.fit_predict(X)

df.to_csv("results/data_clustered.csv", index=False) 
