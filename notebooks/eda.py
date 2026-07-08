import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

print("\n========== DATASET INFO ==========\n")
print(df.info())

print("\n========== DESCRIPTIVE STATISTICS ==========\n")
print(df.describe())

print("\n========== TOP 10 CATEGORIES ==========\n")
print(df["Category"].value_counts())

print("\n========== TOP 10 REGIONS ==========\n")
print(df["Region"].value_counts())

print("\n========== TOTAL SALES ==========\n")
print(df["Sales"].sum())

print("\n========== TOTAL PROFIT ==========\n")
print(df["Profit"].sum())