"""Create python flask wrapper around our buzz generator"""
import os
from flask import Flask
from newsAPP import newsAPI
 


app = Flask(__name__)


@app.route("/")
def generate_news():
    """generate flask wrapper"""
    news  = newsAPI.NewsAPI()
    # page = '<html><body><h1>'
    # page +=  news.getNews()
    # page += '</h1></body></html>'
    # page += 'powered by - newsapi.org'


    page = '<!DOCTYPE html><html><head><style>p {color:blue;}</style></head><body><h1>Technology News for Today</h1><p>'
    page +=  news.getNews()
    page +='</p></body></html>'
    page += 'powered by - newsapi.org'

    return page



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
