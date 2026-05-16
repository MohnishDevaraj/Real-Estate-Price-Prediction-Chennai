import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv(r"..\Data\chennai_clean_step4.csv")

# -----------------------------
# 1. Target Variable Distribution
# -----------------------------
plt.figure()
sns.histplot(df["SALES_PRICE"], kde=True)
plt.title("Distribution of Sales Price")
plt.xlabel("Sales Price")
plt.ylabel("Frequency")
plt.savefig(r"..\Plots\sales_price_distribution.png")
plt.show()

# -----------------------------
# 2. Relationship: Area vs Price
# -----------------------------
plt.figure()
sns.scatterplot(x=df["INT_SQFT"], y=df["SALES_PRICE"])
plt.title("Built-up Area vs Sales Price")
plt.xlabel("Interior Sqft")
plt.ylabel("Sales Price")
plt.savefig(r"..\Plots\area_vs_price.png")
plt.show()

# -----------------------------
# 3. Relationship: House Age vs Price
# -----------------------------
plt.figure()
sns.scatterplot(x=df["HOUSE_AGE"], y=df["SALES_PRICE"])
plt.title("House Age vs Sales Price")
plt.xlabel("House Age (Years)")
plt.ylabel("Sales Price")
plt.savefig(r"..\Plots\house_age_vs_price.png")
plt.show()

# -----------------------------
# 4. Correlation Heatmap (numerical features)
# -----------------------------
numerical_cols = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(12, 10))
sns.heatmap(numerical_cols.corr(), annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig(r"..\Plots\correlation_heatmap.png")
plt.show()