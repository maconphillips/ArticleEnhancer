# Import the required modules
from metascraper import metascraper
from metascraper.aspire import AspireMetaScraper
from bs4 import BeautifulSoup
import requests

# Function to scrape metadata
def scrape_metadata(url):
    # Fetch the webpage content
    response = requests.get(url)
    html = response.content

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Create an instance of the AspireMetaScraper
    scraper = AspireMetaScraper()

    # Scrape the metadata
    metadata = scraper.extract(html, url)

    return metadata

# Example usage
def main():
    url = "sourceURL"
    metadata = scrape_metadata(url)
    print(metadata)

if __name__ == "__main__":
    main()
