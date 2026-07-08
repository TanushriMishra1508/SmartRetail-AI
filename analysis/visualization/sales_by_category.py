import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

# Total Sales by Category
sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/sales_by_category.png", dpi=300)

plt.show()