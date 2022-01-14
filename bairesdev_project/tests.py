from django.test import TestCase
from bairesdev_project.models import News
import sqlite3
import requests
import feedparser

# Create your tests here.

# Request url
def scrape_news(url):
	b = News.objects.all()
	b.delete()
	rss = feedparser.parse(url)
	data = rss.entries
	for news in data:
		data = News(title =  (news.title), link = (news.link), date = (news.published), description = (news.description))
		print (news.description)
		# data.save()



scrape_news("https://rss.app/feeds/HoOgEjAvoWCFXlLS.xml")
# scrape_news("https://rss.app/feeds/JIPx5gwO7Hl5XrjK.xml")
# scrape_news("https://rss.app/feeds/1bRg57t0ngsCXdLB.xml")
