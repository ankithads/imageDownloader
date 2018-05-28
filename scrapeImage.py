from bs4 import BeautifulSoup
import requests
import urllib.request
import random

#url of the page to download the pictures
page_url = 'http://www.boohoo.com/womens/dresses'

print(page_url)

#fetch the url content
page_response = requests.get(page_url, timeout = 5)

#parse the html 
page_content = BeautifulSoup(page_response.content, "html.parser")


#image link will be either in <img> or <picture> <source> tags
#get the image urls and download the images
for link in page_content.find_all('img'):
	try:
		print(link['src'])
		url = link['src']
		if (url.find("http:", 0,len("http:")) != -1):
			print("found")
			url = link['src']
		else:
		file_name = random.randrange(1,10000)
		full_file_name = str(file_name) + '.jpg'
		urllib.request.urlretrieve(url,full_file_name)
	except:
		pass

for link in page_content.find_all('source'):

		print(link['srcset'])
		url = link['srcset']
		if (url.find("http:", 0,len("http:")) != -1):
			print("found")
			url = link['srcset']
		else:
			url = "http:" + link['srcset']
		file_name = random.randrange(1,10000)
		full_file_name = str(file_name) + '.jpg'
		urllib.request.urlretrieve(url,full_file_name)

print("done")