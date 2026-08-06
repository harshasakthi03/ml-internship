import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a simple dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [35, 45, 55, 65, 75]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Features and Target
X = df[["Hours"]]
y = df["Marks"]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 hours of study
prediction = model.predict([[6]])

print("\nPredicted Marks for 6 hours of study:", prediction[0])
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
