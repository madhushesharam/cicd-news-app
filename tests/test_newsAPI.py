"""Test generator.py with pytest"""
import unittest
from newsAPP import newsAPI



def test_news():
    news  = newsAPI.NewsAPI()
    assert len(news.getNews()) != 0
    