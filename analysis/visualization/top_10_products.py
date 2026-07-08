import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

# Top 10 Products by Sales
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# Plot
plt.figure(figsize=(15,8 ))
top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=90, fontsize=8)

plt.subplots_adjust(bottom=0.4)
plt.tight_layout()

plt.savefig("reports/top_10_products.png", dpi=300)

plt.show()