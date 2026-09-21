import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kavi", "Ravi", "Meena"],
    "Age": [20, 21, 20, 22, 21],
    "Mark": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print(df)

print(df.head())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())