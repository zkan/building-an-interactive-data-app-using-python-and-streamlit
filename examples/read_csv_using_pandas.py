import pandas as pd


df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
print(df.columns)
print(df.head(10))
print(df["สถานที่เลี้ยงสัตว์ จังหวัด"].unique())
