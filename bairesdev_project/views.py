from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from bairesdev_project.models import News
from datetime import datetime
import sqlite3
import requests
import feedparser

# Create your views here.

# Main page

def main(request):
	try:
		main_page = render_to_string("bairesdev_project/main_page.html")
		return HttpResponse(main_page)
	except:
		return HttpResponseNotFound("<h1>Go to the main page.</h1>")

# Requesting data from the different pages

def techcrunch(request):
	scrape_news("https://rss.app/feeds/HoOgEjAvoWCFXlLS.xml", "techcrunch")
	news = News.objects.filter(page = "techcrunch")
	return render (request, "bairesdev_project/news.html", {
 		"data" : news
  	})

def mashable(request):
	scrape_news("https://rss.app/feeds/JIPx5gwO7Hl5XrjK.xml", "mashable")
	news = News.objects.filter(page = "mashable")
	return render (request, "bairesdev_project/news.html", {
 		"data" : news
  	})

def theverge(request):
	scrape_news("https://rss.app/feeds/1bRg57t0ngsCXdLB.xml", "theverge")
	news = News.objects.filter(page = "theverge")
	return render (request, "bairesdev_project/news.html", {
 		"data" : news
  	})


 # Scraping

def scrape_news(url, page_name):
	rss = feedparser.parse(url)
	data = rss.entries 					# Getting rss information
	for news in data:
		new = News.objects.filter(title = news.title, link = news.link)			# Validiting existing news
		if new:
			print ("This news already exists.")			# Skiping existing news
		else:
			print ("New info.")							# Adding new news
			datetime_object = datetime.strptime(news.published, '%a, %d %b %Y %H:%M:%S %Z')				# Getting date-time in a valid format
			data = News(page= (page_name), title =  (news.title), link = (news.link), date = (datetime_object), description = (news.description))      # Preparing news for database
			try:
				data.save()				# Commit			
			except:
				print("Error. Saving data in the database.")

def counter (request):
	print ("Algo")