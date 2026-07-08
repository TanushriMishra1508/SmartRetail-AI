import pandas as pd
import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="ISO-8859-1")

print("✅ Dataset Loaded Successfully!")

# -----------------------------
# Business KPIs
# -----------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("\n" + "=" * 45)
print("         BUSINESS INSIGHTS")
print("=" * 45)

print(f"📊 Total Sales     : ${total_sales:,.2f}")
print(f"💰 Total Profit    : ${total_profit:,.2f}")
print(f"🛒 Total Orders    : {total_orders}")
print(f"👥 Total Customers : {total_customers}")

# -----------------------------
# Best Region by Sales
# -----------------------------
region_sales = df.groupby("Region")["Sales"].sum()
best_sales_region = region_sales.idxmax()
best_sales_value = region_sales.max()

# -----------------------------
# Most Profitable Region
# -----------------------------
region_profit = df.groupby("Region")["Profit"].sum()
best_profit_region = region_profit.idxmax()
best_profit_value = region_profit.max()

print("\n🌍 Region Insights")
print("-" * 45)
print(f"🏆 Best Region (Sales)  : {best_sales_region} (${best_sales_value:,.2f})")
print(f"💰 Best Region (Profit) : {best_profit_region} (${best_profit_value:,.2f})")
# -----------------------------
# Top Customer by Sales
# -----------------------------
customer_sales = df.groupby("Customer Name")["Sales"].sum()

top_customer = customer_sales.idxmax()
top_customer_sales = customer_sales.max()

print("\n🏆 Top Customer")
print("-" * 45)
print(f"👤 Customer Name : {top_customer}")
print(f"💵 Total Sales   : ${top_customer_sales:,.2f}")
# -----------------------------
# Best Selling Product
# -----------------------------
product_sales = df.groupby("Product Name")["Sales"].sum()

best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print("\n📦 Best Selling Product")
print("-" * 45)
print(f"🛍️ Product Name : {best_product}")
print(f"💰 Total Sales  : ${best_product_sales:,.2f}")
# -----------------------------
# Best Customer Segment
# -----------------------------
segment_sales = df.groupby("Segment")["Sales"].sum()

best_segment = segment_sales.idxmax()
best_segment_sales = segment_sales.max()

print("\n👥 Best Customer Segment")
print("-" * 45)
print(f"🏆 Segment     : {best_segment}")
print(f"💰 Total Sales : ${best_segment_sales:,.2f}")
# -----------------------------
# Top 10 Loss-Making Products
# -----------------------------
loss_products = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values()
      .head(10)
)

print("\n📉 Top 10 Loss-Making Products")
print("-" * 45)

for product, loss in loss_products.items():
    print(f"{product} : ${loss:,.2f}")
    # -----------------------------
# Save Business Report
# -----------------------------

report = f"""
=========================================
        BUSINESS INSIGHTS REPORT
=========================================

📊 Total Sales      : ${total_sales:,.2f}
💰 Total Profit     : ${total_profit:,.2f}
🛒 Total Orders     : {total_orders}
👥 Total Customers  : {total_customers}

🌍 Best Region (Sales)  : {best_sales_region} (${best_sales_value:,.2f})
💰 Best Region (Profit) : {best_profit_region} (${best_profit_value:,.2f})

🏆 Top Customer
Customer Name : {top_customer}
Total Sales   : ${top_customer_sales:,.2f}

📦 Best Selling Product
Product Name  : {best_product}
Total Sales   : ${best_product_sales:,.2f}

👥 Best Customer Segment
Segment        : {best_segment}
Total Sales    : ${best_segment_sales:,.2f}

📉 Top 10 Loss-Making Products
"""

for product, loss in loss_products.items():
    report += f"{product} : ${loss:,.2f}\n"

with open("reports/business_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\n✅ Business report saved successfully in reports/business_report.txt")