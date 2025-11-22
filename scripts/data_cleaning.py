# data_cleaning.py

# Script to clean the ecommerce dataset for Task 1


import pandas as pd

# Load raw data
df = pd.read_csv("data/data.csv", encoding="latin1")

# Drop null CustomerID values
df = df.dropna(subset=["CustomerID"])

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Create Year column
df["Year"] = df["InvoiceDate"].dt.year

# Create Month column (period format)
df["Month"] = df["InvoiceDate"].dt.to_period("M")

# Identify returns
df["IsReturn"] = df["Quantity"] < 0

# Save cleaned file
df.to_csv("data/cleaned_ecommerce.csv", index=False)

print("Data cleaning completed successfully.")
