import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np


df = pd.read_csv("data_raw.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Binnig

df['tenure_group'] = pd.cut(df['Tenure in Months'], 
                            bins=[-1, 12, 48, 200], 
                            labels=['Newcomer', 'Standard', 'Loyal'])

# Encode categrorical columns 
# (EXCEPT customerID as it has numbers but is not a numeric feature)
label_encoders = {}
for col in df.select_dtypes(include=['object']).columns:
    if col != 'Customer ID' and col != 'tenure_group':
        c = LabelEncoder()
        df[col] = c.fit_transform(df[col])
        label_encoders[col] = c

# Scale numeric features
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])


# PCA

features = [
    'Age', 'Avg Monthly GB Download', 'Churn Score', 'CLTV', 
    'Monthly Charge', 'Number of Referrals', 'Satisfaction Score', 
    'Tenure in Months', 'Total Charges', 'Total Revenue'
]

X = df[features].values

covariance_matrix = np.cov(X.T)

eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

top_2_vectors = np.real(eigenvectors[:, idx[:2]])
pca_result = np.dot(X, top_2_vectors)

df['pca_1'] = pca_result[:, 0]
df['pca_2'] = pca_result[:, 1]

df.to_csv("results/data_preprocessed.csv", index=False)
df.to_csv("data_preprocessed.csv", index=False)