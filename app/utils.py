import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def process_text(text):
    clean_text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return clean_text
