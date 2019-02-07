import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import re
import urllib.request
from urllib.request import urlopen

# url = "https://en.wikipedia.org/wiki/List_of_airlines_of_Africa"
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)

from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_airlines_of_Asia")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

all_countries = []

for link in soup.find_all('a', href=True):
    # print(link['href'])
    # import pdb
    # pdb.set_trace()
    con_lst = link.attrs['href'].__contains__("/wiki/List")
    if con_lst:
    	all_countries.append(link.attrs['href'])


# print(all_countries)

all_airlines_name_code = []

for country in all_countries:
	url = "https://en.wikipedia.org" + str(country)
	try:
		print(url)
		html = urlopen(url)
	
	
		soup = BeautifulSoup(html, "html.parser")
		table = soup.find("table")
		all_head = table.find_all("th")
		
		# head = table.find_all("th"):
		


		for row in table.find_all("tr")[1:]:
			col = row.find_all("td")
			try:
				import pdb
				pdb.set_trace()
				if col[0].contents[0]['title'] and col[4].contents[0]:
					if col[4].contents[0].isupper():
						all_airlines_name_code.append(col[0].contents[0]['title'] + " : " + col[4].contents[0])
					# print(col[0].contents[0]['title'] + " : " + col[2].contents[0])

			except Exception:
				pass
		# print("not available")
	except Exception as e:
		pass

print(all_airlines_name_code)