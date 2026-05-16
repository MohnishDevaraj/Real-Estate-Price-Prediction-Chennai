import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\Chennai_houseing_sale.csv")

# Missing values count
missing_count = df.isnull().sum()

# Missing values percentage
missing_percentage = (missing_count / len(df)) * 100

# Combine into a report
missing_report = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing Percentage': missing_percentage
})

# Show only columns with missing data
missing_report = missing_report[missing_report['Missing Count'] > 0]

print("Missing Values Report:")
print(missing_report.sort_values(by="Missing Percentage", ascending=False))