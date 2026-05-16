import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\chennai_clean_step1.csv")

# -----------------------------
# Handle numerical columns
# -----------------------------
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        median_value = df[col].median()
        df[col].fillna(median_value, inplace = True)

# -----------------------------
# Handle categorical columns
# -----------------------------
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace = True)

# -------------------------------
# Save the cleaned copy
# -------------------------------
df.to_csv("..\Data\chennai_clean_step2.csv", index=False)

print("Missing value handling completed.")
print("Cleaned file saved as: Data/chennai_clean_step2.csv")