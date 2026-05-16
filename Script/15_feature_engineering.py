import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load final dataset
df = pd.read_csv(r"..\Data\chennai_model_ready.csv")

# Remove potential leakage features
leakage_cols = ["REG_FEE", "COMMIS"]
existing = [col for col in leakage_cols if col in df.columns]
df.drop(columns=existing, inplace=True)

# Seperate features and target
X = df.drop(columns=["SALES_PRICE"])
y = df["SALES_PRICE"]

# Train-test split (80-20)
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Gradient Boosting Regressor
model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Get feature importances
importances = model.feature_importances_
feature_names = X.columns

# Create importance DataFrame
importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

# Display top 15 features
print("Top 15 Feature Features:")
print(importance_df.head(15))

# Plot top 15 features
plt.figure(figsize=(10, 6))
plt.barh(importance_df.head(15)["Feature"][::-1], 
         importance_df.head(15)["Importance"][::-1]
)
plt.xlabel("Feature Score")
plt.title("Top 15 Feature Importances from Gradient Boosting Regressor")
plt.tight_layout()
plt.show()

"""
"""

