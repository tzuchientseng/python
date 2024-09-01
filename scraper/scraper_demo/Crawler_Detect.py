from flask import Flask, render_template, request
from crawlerdetect import CrawlerDetect

app = Flask(__name__)
crawler_detect = CrawlerDetect()

@app.route('/')
def hello():
    if crawler_detect.isCrawler(request.headers['User-Agent']):
        return "<h1>你是臭爬蟲</h1>"
    else:
        return "<h1>你不是爬蟲</h1>"

if __name__ == '__main__':
    app.run(port=9998)
