import requests
from bs4 import BeautifulSoup

resp = requests.get('http://sunnytseng.com')
soup = BeautifulSoup(resp.text, 'html.parser')  
list_ = soup.find_all('h2')
for words in list_:
    print(words.text)
print(soup.find_all('h2', 'mb-4'))
print(soup.find_all('h2', {'class':'mb-4'}))
print(soup.find_all('h2', class_ = 'mb-4'))
print(soup.find(id = 'slide3').p.text)


def main():
    resp = requests.get('https://www.dotblogs.com.tw/YiruAtStudio')
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # print(soup.find('h3'))

    main_title = soup.find_all('h3', 'article__title')
    print(main_title)
    print("========")

    B2 = soup.find_all('h3', {'class':'article__title'})
    print(B2)
    print("========")

    B3 = soup.find_all('h3', class_='article__title')
    print(B3)
    print("========")

    for title in B3:
        print(title.a.text)
        print("**********")

if __name__ == '__main__':
    main()
