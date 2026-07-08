import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

# Top 10 Customers by Sales
top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# Plot
plt.figure(figsize=(10, 6))
top_customers.plot(kind="bar")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("reports/top_10_customers.png", dpi=300)

plt.show()