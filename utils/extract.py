import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def scraping_data(BASE_URL):

  data = []
  ## Scraping data untuk semua halaman
  for page in range(1, 51): ### menyesuaikan jumlah halaman
    if page == 1:
      url = BASE_URL
    else:
      url = f"{BASE_URL}/page{page}"
    try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()

      soup = BeautifulSoup(response.text, "html.parser")
      products = soup.select(".collection-card")

      for product in products:
        title = product.select_one(".product-title").text.strip()
        price = product.select_one(".price").text.strip()
        details = product.select(".product-details p")

        rating = details[0].text.strip() if len(details) > 0 else None
        colors = details[1].text.strip() if len(details) > 1 else None
        size = details[2].text.strip() if len(details) > 2 else None
        gender = details[3].text.strip() if len(details) > 3 else None

        data.append({
          "title": title, "price":price, "rating":rating,
          "colors": colors, "size": size, "gender":gender, "timestamp": datetime.now()
        })
      print(f"Page {page} selesai.")
    except Exception as e:
      print(f"page {page} error: {e}")
  
  df = pd.DataFrame(data)

  return df
