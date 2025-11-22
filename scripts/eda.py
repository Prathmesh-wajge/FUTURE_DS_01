# eda.py
# ----------------------------------------------------
# Exploratory Data Analysis for ecommerce dataset
# ----------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_ecommerce.csv")

# ===============================
# 1. Basic Info
# ===============================
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())

# ===============================
# 2. Top products
# ===============================
top_products = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 products:\n", top_products)

# ===============================
# 3. Sales by country
# ===============================
country_sales = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)
print("\nTop 10 Countries:\n", country_sales.head(10))

plt.figure(figsize=(10, 5))
country_sales.head(10).plot(kind="bar")
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ===============================
# 4. Monthly Trend
# ===============================
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["TotalPrice"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ===============================
# 5. Returns Analysis
# ===============================
returns = df[df["IsReturn"] == True]
top_returns = (
    returns.groupby("Description")["Quantity"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop Returned Products:\n", top_returns)

print("\nEDA Completed.")
