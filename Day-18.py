import requests
from bs4 import BeautifulSoup

def fetch_webpage_title(url):
    """
    Fetches and prints the title of a webpage.
    
    Args:
        url (str): The URL of the webpage.
        
    Returns:
        str: The title of the webpage or an error message if unable to fetch.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title found"
        return title
    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"

# Test the function with the given URL
test_url = 'https://example.com'
print(fetch_webpage_title(test_url))
