import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")

# Create Month-Year column
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

# Plot
plt.figure(figsize=(12,6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("reports/monthly_sales_trend.png", dpi=300)

plt.show()