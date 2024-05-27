import requests
url = 'https://tzuchientseng.github.io/sunny.github.io/'
htmlfile = requests.get(url)
print(htmlfile.text)
