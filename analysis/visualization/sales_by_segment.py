import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

# Sales by Customer Segment
segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

# Plot
plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/sales_by_segment.png", dpi=300)

plt.show()