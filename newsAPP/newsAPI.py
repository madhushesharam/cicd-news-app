import requests
import json
import os
from newsapi import NewsApiClient
from datetime import datetime, timedelta

class NewsAPI:
    def __init__(self):
         pass
               
       
    def getNews(self):
        newsapi = NewsApiClient(api_key = os.environ["API_KEY"])
        all_articles = newsapi.get_everything(q = 'technology',
                        sources = 'bbc-news,the-verge',
                        domains = 'bbc.co.uk,techcrunch.com',
                        from_param = datetime.strftime(
                        datetime.now() - timedelta(10), '%Y-%m-%d'),
                        to = datetime.today().strftime('%Y-%m-%d'),
                        language = 'en',
                        sort_by = 'relevancy',
                        page = 1)

        return all_articles['articles'][0]['description']

        



  