# Student Grade Prediction using Machine Learning (Python)

A beginner-friendly **machine learning project in Python** that predicts a student's **final grade (G3, out of 20)** from study time, past failures, absences, parents' education, and earlier grades. Built with **pandas, scikit-learn, and matplotlib** using the UCI Student Performance dataset.

**Keywords:** student performance prediction, grade prediction, educational data mining, linear regression, scikit-learn, pandas, matplotlib, Python machine learning project for beginners.

## Objective

To build a simple, practical model that estimates a student's final grade, so teachers could spot students who may need support early.

## Dataset

- **Source:** [UCI Machine Learning Repository: Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance) (math class file `student-mat.csv`)
- **Size:** [395] students, [33] attributes
- **Target:** `G3` (final grade). `G1` and `G2` are earlier-period grades.
- Credit to the dataset creators (P. Cortez and A. Silva, University of Minho, Portugal).

## Tools

- Python
- pandas (data handling)
- scikit-learn (Linear Regression, train/test split, metrics)
- matplotlib (charts)

## Method

1. Load the CSV data with pandas.
2. Select features: study time, failures, absences, parents' education, going out, health, and optionally G1 and G2.
3. Split the data: 80% training, 20% testing.
4. Train a Linear Regression model.
5. Evaluate with Mean Absolute Error and R² score.
6. Plot actual vs predicted grades and predict for a new student.

## Results

- Average error: [your value] grade points
- R² score: [your value]
- Most influential factors: [your top 2-3 factors]
- Chart: `results.png` (actual vs predicted grades)

**Key finding:** earlier grades (G1, G2) are the strongest predictors of the final grade. Without them, predictions are noticeably less accurate. [Add both scores if you tested this.]

## How to run

1. Install Python from python.org.
2. Install the libraries:
   ```
   py -m pip install pandas scikit-learn matplotlib
   ```
   (On Mac/Linux use `python3 -m pip install ...`.)
3. Put `predict_grades.py` and `student-mat.csv` in the same folder.
4. Run:
   ```
   py predict_grades.py
   ```
5. To try predicting without earlier grades, set `USE_PREVIOUS_GRADES = False` at the top of the script.

## Limitations

- Small dataset from two schools in Portugal.
- Linear Regression is simple and can miss complex patterns.
- Predictions are estimates and should support, not replace, teachers' judgment.

## Future improvements

- Compare with Random Forest and other models.
- Add the Portuguese-class dataset.
- Build a simple interface for teachers to enter details and get a prediction.

## Author

GitHub: [friendlyg602-boop](https://github.com/friendlyg602-boop)
