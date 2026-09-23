import pandas as pd

data = {
    "Name": ["suba", "sandy", "gayathri", "revathi", "vishnu", "sriharini"],
    "Age": [20, 21, 20, 22, 21, 20],
    "Mark": [85, 90, 78, 88, 95, 85]
}

df = pd.DataFrame(data)

print(df)

print(df.sort_values("Mark", ascending=False))

print(df["Age"].unique())

print(df["Age"].nunique())

print(df["Age"].value_counts())

print(df["Mark"].mean())

print(df["Mark"].median())

print(df["Mark"].min())

print(df["Mark"].max())

print(df.isnull().sum())

print(df.duplicated())

df = df.drop_duplicates()

df["Age"] = df["Age"].astype(int)

print(df.groupby("Age")["Mark"].mean())

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    else:
        return "C"

df["Grade"] = df["Mark"].apply(grade)

print(df)