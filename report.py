import sqlite3
import pandas as pd

conn = sqlite3.connect("prices.db")

query = "SELECT * FROM products"

df = pd.read_sql_query(query, conn)

print(df)

df.to_csv("product_report.csv", index=False)

print("\nReport generated: product_report.csv")

conn.close()