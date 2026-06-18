# Competitor Price Monitor

A Python-based web scraping project that extracts product pricing data from an e-commerce website, stores the data in SQLite, and generates reports.

## Features

- Web scraping using Requests and BeautifulSoup
- Store product data in SQLite
- Query and view stored products
- Generate CSV reports using Pandas

## Technologies

- Python
- Requests
- BeautifulSoup4
- SQLite3
- Pandas

## Project Structure

competitor-price-monitor/
├── scraper.py
├── database.py
├── view_data.py
├── report.py
├── requirements.txt
└── README.md

## How to Run

python database.py
python scraper.py
python view_data.py
python report.py

## Example Output

| Product Name         | Price  |
| -------------------- | ------ |
| A Light in the Attic | £51.77 |
| Tipping the Velvet   | £53.74 |
