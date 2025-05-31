import requests
from bs4 import BeautifulSoup

def search_news(keyword):
    url = f"https://www.example-news-website.com/search?q={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article', class_='news-item')
    results = []

    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        results.append({'title': title, 'link': link})

    return results

keyword = "your_search_keyword"
news = search_news(keyword)

for item in news:
    print(item['title'], item['link'])
