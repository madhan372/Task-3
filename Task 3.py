# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Function to perform web scraping
def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extracting titles and links from articles
        articles = soup.find_all('article')
        
        for article in articles:
            # Extract title
            title_element = article.find('h2')
            if title_element:
                title = title_element.text.strip()
                print(f"Title: {title}")
                
            # Extract link
            link_element = article.find('a')
            if link_element:
                link = link_element['href']
                print(f"Link: {link}")
                
            print()  # Print an empty line for separation

    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

