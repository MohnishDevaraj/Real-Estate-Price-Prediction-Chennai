import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load final dataset
df = pd.read_csv(r"..\Data\chennai_model_ready.csv")

# ------------------------------
# Seperate features and target
# ------------------------------
X = df.drop(columns=["SALES_PRICE"])
y = df["SALES_PRICE"]

# ------------------------------
# Train-test split (80-20)
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# Train Linear Regression model
# ------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------
# Predictions
# ------------------------------
y_pred = model.predict(X_test)

# ------------------------------
# Evaluation
# ------------------------------
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Linear Regression Baseline Performance:")
print("---------------------------------------")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")