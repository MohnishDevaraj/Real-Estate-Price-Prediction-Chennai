import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\Chennai_houseing_sale.csv")

# Identify categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns

print("Categorical Columns:")
print(categorical_columns)

# Show unique values for each categorical column
for col in categorical_columns:
    print(f"\nColumn: {col}")
    print(df[col].value_counts())