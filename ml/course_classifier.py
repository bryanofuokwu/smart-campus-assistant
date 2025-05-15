from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Example student data: [GPA, hours_studied_per_week, prefers_theory (1/0)]
data = [
    [3.9, 10, 1, 'CS'],
    [3.0, 25, 0, 'Math'],
    [3.5, 15, 1, 'CS'],
    [3.2, 20, 0, 'Math'],
    [3.8, 12, 1, 'CS'],
    [2.9, 30, 0, 'Math'],
    [3.7, 18, 1, 'CS'],
    [3.1, 22, 0, 'Math']
]

df = pd.DataFrame(data, columns=['GPA', 'StudyHours', 'PrefersTheory', 'Label'])
X = df[['GPA', 'StudyHours', 'PrefersTheory']]
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Prediction for new student [3.6 GPA, 14 hours, prefers theory]:",
      clf.predict([[3.6, 14, 1]])[0])