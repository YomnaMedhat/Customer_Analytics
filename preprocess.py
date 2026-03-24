import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


df = pd.read_csv("data_raw.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Encode categrorical columns 
# (EXCEPT customerID as it has numbers but is not a numeric feature)
label_encoders = {}
for col in df.select_dtypes(include=['object']).columns:
    if col != 'customerID':
        c = LabelEncoder()
        df[col] = c.fit_transform(df[col])
        label_encoders[col] = c

# Scale numeric features
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

df.to_csv("data_preprocessed.csv", index=False)