import pandas as pd

# Load the data
df = pd.read_csv(r"..\Data\Chennai_houseing_sale.csv")

# -----------------------------
# Standardize text columns
# -----------------------------
text_columns = df.select_dtypes(include=['object']).columns

for col in text_columns:
    df[col] = df[col].str.strip().str.title()

# -------------------------------
# Fix known categorical issues
# -------------------------------

# AREA typos
df["AREA"] = df["AREA"].replace({
    "Chrompt" : "Chrompet",
    "Chrmpet" : "Chrompet",
    "Karapakam" : "Karapakkam",
})

# SALE_COND inconsistencies
df["SALE_COND"] = df["SALE_COND"].replace({
    "Ab Normal" : "Abnormal"
})

# UTILITY_AVAIL inconsistencies
df["UTILITY_AVAIL"] = df["UTILITY_AVAIL"].replace({
    "Nosewr" : "No Sewr",
    "Nosewa" : "No Sewa",
    "Allpub" : "All Pub"
})

# PARK_FACIL consistency
df["PARK_FACIL"] = df["PARK_FACIL"].replace({
    "Yes" : "Yes",
    "No" : "No"
})

# -------------------------------
# Save the cleaned copy
# -------------------------------
df.to_csv("..\Data\chennai_clean_step1.csv", index=False)

print("Categorical cleaning completed.")
print("Cleaned file saved as: Data/chennai_clean_step1.csv")