import requests
from bs4 import BeautifulSoup
# from app import myfn

def main():
    pass
    url = 'https://tw-nba.udn.com/nba/index'

    text = get_tag_text(url, 'h1')
    for line in text:
        print(line.text)

def get_tag_text(url, tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text,'html.parser')
            # return soup.find(tag).text
            return soup.find_all(tag)
    except Exception as e:
        print('Exception:%s' % (e))
    return None


if __name__ == '__main__':
    main()