from datasets import load_dataset
import pandas as pd

dataset = load_dataset("muqsith123/telco-customer-churn")

df = pd.DataFrame(dataset["train"])

df.to_csv("telco_customer_churn.csv", index=False)