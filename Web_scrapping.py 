import requests
from bs4 import BeautifulSoup

# Website URL
url = input("Enter website URL (example: https://example.com): ")

try:
    # Send request to website
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all headings (h1, h2, h3)
    print("\n--- Extracted Headings ---")
    headings = soup.find_all(['h1', 'h2', 'h3'])

    if headings:
        for i, heading in enumerate(headings, 1):
            print(f"{i}. {heading.text.strip()}")
    else:
        print("No headings found on this page.")

except requests.exceptions.RequestException as e:
    print("Error fetching the website:", e)