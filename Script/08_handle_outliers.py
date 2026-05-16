import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\chennai_clean_step3.csv")

# -----------------------------
# Identify numerical columns
# -----------------------------
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

# -----------------------------
# Apply IQR-based capping
# -----------------------------
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

# -------------------------------
# Save the cleaned dataset
# -------------------------------
df.to_csv("..\Data\chennai_clean_step4.csv", index=False)

print("Outlier handling completed using IQR capping.")
print("Final cleaned dataset saved as: Data/chennai_clean_step4.csv")