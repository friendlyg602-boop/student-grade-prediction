"""
Student grade predictor

Dataset: UCI "Student Performance" (student-mat.csv, math class)
Download: https://archive.ics.uci.edu/dataset/320/student+performance
Unzip it and put student-mat.csv in the same folder as this script.

Install once:  pip install pandas scikit-learn matplotlib
Run:           python predict_grades.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Try switching this to False to see a harder (more realistic) problem:
# predicting the final grade WITHOUT knowing earlier grades.
USE_PREVIOUS_GRADES = True

# ---------- 1. Load the data ----------
df = pd.read_csv("student-mat.csv", sep=";")  # this file uses ; not ,
print("Rows, columns:", df.shape)
print(df[["G1", "G2", "G3", "studytime", "failures", "absences"]].head())

# ---------- 2. Choose features (inputs) and target (output) ----------
features = ["studytime", "failures", "absences", "Medu", "Fedu", "goout", "health"]
if USE_PREVIOUS_GRADES:
    features += ["G1", "G2"]  # G1, G2 = grades from earlier periods

X = df[features]
y = df["G3"]  # G3 = final grade (0-20)

# ---------- 3. Split into training and testing sets ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------- 4. Train the model ----------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------- 5. Evaluate ----------
predictions = model.predict(X_test)
print("\nAverage error (grade points):", round(mean_absolute_error(y_test, predictions), 2))
print("R² score (1.0 = perfect):", round(r2_score(y_test, predictions), 2))

# ---------- 6. What matters most? ----------
print("\nFeature effects (positive = raises predicted grade):")
for name, coef in sorted(zip(features, model.coef_), key=lambda p: -abs(p[1])):
    print(f"  {name:10s} {coef:+.2f}")

# ---------- 7. Plot actual vs predicted ----------
plt.scatter(y_test, predictions, alpha=0.6)
plt.plot([0, 20], [0, 20], color="red", linestyle="--")  # perfect-prediction line
plt.xlabel("Actual final grade")
plt.ylabel("Predicted final grade")
plt.title("Actual vs predicted final grades")
plt.savefig("results.png")
plt.show()

# ---------- 8. Predict for a new student ----------
new_student = pd.DataFrame([{
    "studytime": 3, "failures": 0, "absences": 4,
    "Medu": 3, "Fedu": 3, "goout": 2, "health": 4,
    **({"G1": 12, "G2": 13} if USE_PREVIOUS_GRADES else {}),
}])
predicted = model.predict(new_student[features])[0]
print(f"\nPredicted final grade for new student: {predicted:.1f} / 20")
