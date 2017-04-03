import get_result

def filter_bloomberg():
	url = 'http://www.bloomberg.com/'
	titles,links,big_title,big_link = get_result.results()
	news = {}
	for i in range(len(big_title)):
		news[big_title[i].lower()]=url+big_link[i]
	us = ['fed','bank','dow','u.s.','dollar']
	china = ['china','hong kong']
	index= ['home','bond','yield','inflation']
	commodity = ['oil','gold']
	europe = ['ecb','boe','draghi','prime minister','england','uk','eu','euro','brexit']
	japan = ['boj','japan']
	others =['australia','new zealand']
	list_ = us+china+commodity+europe+japan+others+index
	for i in range(len(titles)):

		if any(word in titles[i].lower() for word in list_):

			news[titles[i].lower()]=url+links[i]
	return news