"""
Using API
"""
import requests

def google_search(query, api_key, cse_id, num_results=10):
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
        'num': num_results
    }
    
    response = requests.get(search_url, params=params)
    results = response.json()
    
    if 'items' not in results:
        return "No results found."
    
    return results['items']

# 替換以下的 API_KEY 和 CSE_ID 為你自己的
API_KEY = 'YOUR_API_KEY'
CSE_ID = 'YOUR_CSE_ID'

query = "Python programming"
results = google_search(query, API_KEY, CSE_ID)

for i, result in enumerate(results):
    print(f"Result {i+1}:")
    print(f"Title: {result['title']}")
    print(f"Snippet: {result['snippet']}")
    print(f"Link: {result['link']}\n")

"""
Using scraper
"""
import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {
        'q': query
    }
    
    response = requests.get('https://duckduckgo.com/html/', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for result in soup.find_all('a', class_='result__a'):
        title = result.text
        link = result['href']
        results.append({
            'title': title,
            'link': link
        })
    
    return results

query = "Python programming"
results = duckduckgo_search(query)

for i, result in enumerate(results):
    print(f"Result {i+1}:")
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}\n")
