import requests
from bs4 import BeautifulSoup
import json
import random
from datetime import datetime

def scrape_brand_data():
    # Osnovni URL sandbox okolja
    BASE_URL = "https://web-scraping.dev/products"
    
    print("Zagon zajema podatkov...")
    
    # 1. PRIDOBIVANJE IZDELKOV (Products)
    # Simuliramo zajem - v praksi bi tukaj uporabili requests.get(BASE_URL)
    products = [
        {"name": "Pro Gaming Mouse", "price": "$59.99"},
        {"name": "Mechanical Keyboard", "price": "$120.00"},
        {"name": "UltraWide Monitor", "price": "$350.00"}
    ]

    # 2. PRIDOBIVANJE PRIČEVANJ (Testimonials)
    testimonials = [
        {"user": "Ana K.", "text": "Najboljša nakupovalna izkušnja do zdaj!"},
        {"user": "Marko P.", "text": "Zelo hitra dostava in kakovostni izdelki."}
    ]

    # 3. PRIDOBIVANJE MNENJ (Reviews) - Ključni del za 2023
    reviews = []
    sample_reviews = [
        "Amazing quality, really impressed!",
        "Disappointed with the shipping time.",
        "Excellent customer support and product.",
        "The build quality is average for the price.",
        "Simply the best on the market!"
    ]
    
    # Ustvarimo naključne podatke za leto 2023 za demonstracijo
    # V realnem scenariju bi tukaj uporabili BeautifulSoup za iskanje po HTML-ju
    for month in range(1, 13):
        for _ in range(3): # 3 mnenja na mesec
            day = random.randint(1, 28)
            date_obj = datetime(2023, month, day)
            reviews.append({
                "text": random.choice(sample_reviews),
                "date": date_obj.strftime('%Y-%m-%d'),
                "month_year": date_obj.strftime('%b %Y')
            })

    # Shranjevanje v JSON
    final_data = {
        "products": products,
        "testimonials": testimonials,
        "reviews": reviews
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    
    print("Podatki so uspešno shranjeni v data.json!")

if __name__ == "__main__":
    scrape_brand_data()