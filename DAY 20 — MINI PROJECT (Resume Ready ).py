import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data
data = {
    "Hours": [1,2,3,4,5,6,7,8],
    "Result": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = LogisticRegression()
model.fit(X, y)

# User input
hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

if prediction == 1:
    print("Result: Pass ")
else:
    print("Result: Fail ")