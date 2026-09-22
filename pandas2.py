import pandas as pd

data = {
    "Name": ["Sarva", "gayathri", "Vimal", "Velan", "Vishnu"],
    "Age": [20, 21, 20, 22, 21],
    "Mark": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print(df["Name"])

print(df[["Name", "Mark"]])

print(df.loc[0])

print(df.iloc[1])

print(df[df["Mark"] > 80])

print(df[(df["Age"] == 21) & (df["Mark"] > 80)])

print(df[df["Name"].isin(["Sarva", "gayathri"])])
