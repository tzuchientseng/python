import requests
from bs4 import BeautifulSoup
import re 

def main():
    resp = requests.get('https://sunnytseng.com')
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))
    print(soup.find('a', {'data-foo': 'mac-foo'})) # 特殊字元 使用 diect 取得元件
    for title in soup.find_all(re.compile('h[1-6]')):
        print(title.text.strip())

    imgs = soup.find_all('img')
    # type 1
    for img in imgs:
        if 'src' in img.attrs:
            if img['src'].endswith('.png'):
                print(img['src'])
    # type 2
    for img in soup.find_all('img', {'src': re.compile('.jpg')}):
        print(img['src'])


    resp = requests.get('https://sunnytseng.com')
    soup = BeautifulSoup(resp.text, 'html.parser')

    rowa = soup.find('table', 'table') # 第一個表標籤 第二個表類別
    rowb = rowa.tbody.find_all('tr')

    for row in rowb:
        print(row.find_all('td')[2].text) # 指定第幾個td (index=0 開始)

if __name__ == '__main__':
    main()
