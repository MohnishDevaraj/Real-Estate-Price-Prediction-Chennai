import pandas as pd

# Load the cleaned dataset
df = pd.read_csv(r"..\Data\chennai_clean_step4.csv")

# -----------------------------
# 1. Drop non-predictive ID Columns
# -----------------------------
df.drop(columns=["PRT_ID"], inplace=True)

# -----------------------------
# 2. Seperate categorical & numerical columns
# -----------------------------
categorical_cols = df.select_dtypes(include=["object"]).columns

# -----------------------------
# 3. One-hot encode categorical variables
# -----------------------------
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# -------------------------------
# 4. Save encoded dataset
# -------------------------------
df_encoded.to_csv("..\Data\chennai_model_ready.csv", index=False)

print("Feature preparation completed.")
print("Model-ready dataset saved as: Data/chennai_model_ready.csv")