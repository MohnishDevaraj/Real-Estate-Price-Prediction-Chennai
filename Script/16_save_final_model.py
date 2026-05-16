import pandas as pd
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Load final dataset
df = pd.read_csv(r"..\Data\chennai_model_ready.csv")

# Remove potential leakage columns
leakage_cols = ["REG_FEE", "COMMIS"]
existing = [col for col in leakage_cols if col in df.columns]
df.drop(columns=existing, inplace=True)

# Seperate features and target
X = df.drop(columns=["SALES_PRICE"])
y = df["SALES_PRICE"]

# Train-test split (80-20)
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Gradient Boosting Regressor
final_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05, max_depth=3, random_state=42)
final_model.fit(X_train, y_train)

# -----------------------------
# Save the model
# -----------------------------
with open("../Models/gradient_boosting_model.pkl", "wb") as f:
    pickle.dump(final_model, f)

# -----------------------------
# Save feature columns
# -----------------------------
with open("../Models/col_feature_columns.txt", "w") as f:
    for col in X.columns:
        f.write(col + "\n")

print("Final model saved as: Models/gradient_boosting_model.pkl")
