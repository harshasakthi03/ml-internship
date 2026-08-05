import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("train.csv")

print(df.head())
print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop("Cabin", axis=1, inplace=True)
print(df.isnull().sum())
sns.countplot(x="Survived", data=df)

plt.show()
sns.countplot(x="Sex", data=df)

plt.show()
plt.hist(df["Age"])

plt.title("Age Distribution")

plt.show()
sns.countplot(x="Pclass", data=df)

plt.show()
sns.countplot(x="Pclass", data=df)

plt.show()
sns.countplot(x="Sex", hue="Survived", data=df)

plt.show()
df.to_csv("cleaned_titanic.csv", index=False)