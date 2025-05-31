# pip install beautifulsoup4 requests
from bs4 import BeautifulSoup
import os

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_html(content):
    return BeautifulSoup(content, 'html.parser')

def get_titles(soup):
    titles = soup.find_all('title')
    return [title.get_text() for title in titles]

def get_divs_by_class(soup, class_name):
    divs = soup.find_all('div', class_=class_name)
    return [div.get_text() for div in divs]

def get_links(soup):
    links = soup.find_all('a')
    return [(link.get('href'), link.get_text()) for link in links]

def main():
    # 獲取文件路徑
    fn = os.path.join(os.path.dirname(__file__), 'output.txt')

    # 讀取並解析HTML文件
    html_content = read_html_file(fn)
    soup = parse_html(html_content)

    # 提取所有的標題
    titles = get_titles(soup)
    print("Titles:")
    for title in titles:
        print(title)

    # 提取特定類別的div標籤
    specific_class = 'specific-class'  # 修改成你需要的class名稱
    divs = get_divs_by_class(soup, specific_class)
    print("\nDivs with class '{}':".format(specific_class))
    for div in divs:
        print(div)

    # 提取所有的連結
    links = get_links(soup)
    print("\nLinks:")
    for href, text in links:
        print(href, text)

if __name__ == "__main__":
    main()
