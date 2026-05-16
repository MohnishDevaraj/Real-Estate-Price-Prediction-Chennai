import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\chennai_clean_step2.csv")

# -----------------------------
# Convert 'date' column to datetime format
# -----------------------------
df["DATE_SALE"] = pd.to_datetime(df["DATE_SALE"], errors="coerce", dayfirst=True)
df["DATE_BUILD"] = pd.to_datetime(df["DATE_BUILD"], errors="coerce", dayfirst=True)

# -----------------------------
# Extract useful features
# -----------------------------
df["SALE_YEAR"] = df["DATE_SALE"].dt.year
df["BUILD_YEAR"] = df["DATE_BUILD"].dt.year

# House age at sale time
df["HOUSE_AGE"] = df["SALE_YEAR"] - df["BUILD_YEAR"]

# -------------------------------
# Drop original date columns
# -------------------------------
df.drop(columns=["DATE_SALE", "DATE_BUILD"], inplace=True)

# -------------------------------
# Save dataset
# -------------------------------
df.to_csv("..\Data\chennai_clean_step3.csv", index=False)

print("Date feature engineering completed.")
print("New features added: SALE_YEAR, BUILD_YEAR, HOUSE_AGE")
print("Cleaned file saved as: Data/chennai_clean_step3.csv")