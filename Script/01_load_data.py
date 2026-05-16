import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\Chennai_houseing_sale.csv")

# Basic inspection
print("Dataset Shape:", df.shape)
print("\nColumn names:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())