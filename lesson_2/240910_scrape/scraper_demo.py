import requests
from bs4 import BeautifulSoup

def main():
    url1 = 'https://www.cakenobel.com.tw/' 
    bad_url = 'https://www.aacakenobel.com.tw/111' #不存在url
    
    text1 = get_tag_text(url1, 'h1') 
    print(text1) 
    #可正常找到<h1></h1>
    
    text2 = get_tag_text(url1, 'h2') 
    print(text2) 
    #找不到h2，回傳None
    
    text3 = get_tag_text(bad_url, 'h1') 
    print(text3) 
    #找不到url，所以回傳錯誤原因

def get_tag_text(url, tag): 
    try:
        resp = requests.get(url)
        if resp.status_code == 200: 
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(tag).text #有找到，回傳找到文字
    except Exception as e: 
        print('Exception: %s' %(e)) #錯誤原因 
    return None #找不到元素

if __name__ == '__main__': 
    main()
