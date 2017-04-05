#find links and titles from bloomberg html code

from bs4 import BeautifulSoup
import urllib2
from collections import defaultdict

def results():
	#get data
	URL='http://www.bloomberg.com/markets'
	req = urllib2.Request(URL,
								headers={'User-Agent': "Resistance is futile"})
	response = urllib2.urlopen(req)
	#parsing html
	soup = BeautifulSoup(response,'html.parser')
	titles=[]
	links = []
	big_titles=[]
	big_links = []
	results = soup.findAll("li", {"class" : "top-news-v3-story-view"})
	for result in results:
		titles.append(result.h1.text)
		links.append(result.h1.a.get('href'))
	results = soup.findAll("li", {"class" : "hero-v2__related-news-stories-item"})
	for result in results:
		titles.append(result.a.text)
		links.append(result.a.get('href'))
	results = soup.findAll("div", {"class" : "hero-v2-big-story__information theme__border-color"})
	for result in results:
		big_titles.append(result.a.text)
		big_links.append(result.a.get('href'))
	results = soup.findAll("div", {"class" : "two-up-story-view"})
	for result in results:
		big_titles.append(result.article.div.a.text)
		big_links.append(result.article.div.a.get('href'))

	results = soup.findAll("div", {"class" : "three-up-story-view"})
	for result in results:
		titles.append(result.article.div.a.text)
		links.append(result.article.div.a.get('href'))

	return titles,links,big_titles,big_links


