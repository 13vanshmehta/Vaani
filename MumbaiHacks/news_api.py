import requests
from bs4 import BeautifulSoup
import json
import schedule
import time
from datetime import datetime

# Base URL for Google News RSS feed with search parameters
BASE_URL = 'https://news.google.com/rss/search'

# Function to fetch news headlines related to a product in a specific region
def fetch_news_headlines(region, product):
    params = {
        'q': f"{product} {region}",
        'gl': 'IN',          # Specify India as the region
        'ceid': 'IN:en'      # Customize for India; change language if needed
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        articles = soup.find_all('item')
        
        # Parsing news headlines
        news_data = []
        for article in articles:
            headline = article.title.text
            link = article.link.text
            pub_date = article.pubDate.text
            
            news_data.append({
                'headline': headline,
                'link': link,
                'publication_date': pub_date
            })
        
        return news_data
    else:
        print("Failed to fetch data:", response.status_code)
        return None

# Function to save the news headlines to a JSON file
def save_news_to_json(region, product, news_data):
    filename = f"{region}_{product}_news_{datetime.now().strftime('%Y%m%d%H%M')}.json"
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(news_data, json_file, ensure_ascii=False, indent=4)
    print(f"News data saved to {filename}")

# Main function to execute data fetching and saving
def main(region, product):
    news_data = fetch_news_headlines(region, product)
    if news_data:
        save_news_to_json(region, product, news_data)

# Schedule the script to run every 6 hours
def schedule_news_scraper():
    region = 'Mumbai'   # Change this to the desired region
    product = 'Smartphone'   # Change this to the desired product
    
    schedule.every(6).hours.do(main, region=region, product=product)
    
    print("Starting news headline fetch scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Check every second for scheduled tasks

# Run the scheduler
if __name__ == "__main__":
    schedule_news_scraper()
