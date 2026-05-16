import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\Chennai_houseing_sale.csv")

print("Dataset Info:")
print(df.info())

print("\nSummary Statistics (Numerical Columns):")
print(df.describe())