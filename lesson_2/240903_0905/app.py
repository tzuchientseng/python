import requests
from bs4 import BeautifulSoup

url = 'https://tw-nba.udn.com/nba/index'
resp = requests.get(url)
# print(resp.text) # 200

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
# print(soup.prettify())

# geth1 = soup.find('h1').text # 不含標籤
geth1_list = soup.find_all('h1') 
for h1 in geth1_list:
    print(h1.text)  # 輸出每個 <h1> 標籤中的文字

getp = soup.find('p').text
print(getp)


def myfn():
    pass

# print('name:', __name__) # __main__ or app (被呼叫)

if __name__ == '__main__':
    print('name:', __name__) # __main__
