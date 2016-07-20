import requests
import sys
from bs4 import BeautifulSoup
url='http://www.imdb.com'
main_response=requests.get(url)
main_soup=BeautifulSoup(main_response.text,'lxml')
main_divs=main_soup.find_all('div',{'class':'title'})
visited={}
cot=0
bool_exit=0
f=open('movieList.txt','w+')
def increment():
	global cot
	cot=cot+1
def total_movies():
	global bool_exit
	bool_exit=1
	sys.exit()
def crawl(url2):
	response=requests.get(url2)
	soup=BeautifulSoup(response.text,'lxml')
	try:
		rating=soup.find('span',{'itemprop':'ratingValue'}).text
		title=soup.find('h1',{'itemprop':'name'}).text
		if float(rating)>float(7):
			increment()
			f.write(title+rating+'\n')
			print(cot,title,rating)
		if float(cot)>float(199):
			f.close()	
			total_movies()
	except:
		if float(bool_exit)!=float(0):
			sys.exit()
		pass
	child=soup.find_all('div',{'class':'rec_item'})
	for i in child:
		id=i.get('data-tconst')
		if id in visited:
			continue
		else:
			visited[id]=1

		link=i.find('a').get('href')
		link=url+link
		crawl(link)
for item in main_divs:
	link=item.find('a').get('href')
	link=url+link
	crawl(link)
