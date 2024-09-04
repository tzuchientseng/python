import requests
from bs4 import BeautifulSoup

url = 'https://tw-nba.udn.com/nba/index'
resp = requests.get(url)
# resp = requests.get(url) 
# print(resp.text) # 200

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
# print(soup.prettify())

geth1 = soup.find('h1').text # 不含標籤
print(geth1)

getp = soup.find('p').text
print(getp)
