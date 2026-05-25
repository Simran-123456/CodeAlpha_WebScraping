import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "http://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store data
books = []
prices = []

# Find all books
book_data = soup.find_all("article", class_="product_pod")

for item in book_data:
    # Book title
    title = item.h3.a["title"]

    # Price
    price = item.find("p", class_="price_color").text

    books.append(title)
    prices.append(price)

# Create DataFrame
df = pd.DataFrame({
    "Book Title": books,
    "Price": prices
})

# Print output
print(df)

# Save CSV file
df.to_csv("scraped_books.csv", index=False)

print("Web Scraping Completed Successfully!")