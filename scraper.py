import requests
import sqlite3
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

conn = sqlite3.connect("prices.db")
cursor = conn.cursor()

for book in books[:10]:

    title = book.h3.a["title"]

    price = (
        book.find("p", class_="price_color")
        .text
        .replace("£", "")
        .replace("Â", "")
    )

    cursor.execute(
        """
        INSERT INTO products
        (name, price, rating)
        VALUES (?, ?, ?)
        """,
        (title, float(price), "N/A")
    )

    print(f"Added: {title}")

conn.commit()
conn.close()

print("\nData saved to database")