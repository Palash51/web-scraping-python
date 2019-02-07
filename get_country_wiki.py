# https://en.wikipedia.org/wiki/Lists_of_countries_and_territories

import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://en.wikipedia.org/wiki/List_of_sovereign_states"

response = requests.get(url)

# soup = BeautifulSoup(response.text)

# # print(soup)

# for link in soup.find_all('a', href=True):
# 	title = link.get('title')
# 	if title and title.isalpha():
# 		# print(title)



soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all("table", class_="sortable wikitable")
# print(tables)
all_countries_dict = {}
all_countries = []
count = 0
table = soup.find("table",class_="sortable wikitable")
for items in table.find_all("tr")[1:-1]:
    data = [' '.join(item.text.split()) for item in items.find_all(['th','td'])]
    # print(data[0] +"------>" + data[1])
    if data[1] and data[1].__contains__("UN"):
	    	all_countries.append(data[0])
	    	count = count + 1
	    	# print(data[0])

	    	alphabet = data[0][0].lstrip('ZZZ').lower()
	    	if alphabet:
	    		# import pdb
	    		# pdb.set_trace()
	    		if alphabet in all_countries_dict.keys():
	    			c_lst.append(data[0].split("–")[0].lstrip('ZZZ'))
	    			
	    		else:
	    			c_lst = [data[0].split("–")[0].lstrip('ZZZ')]
	    			all_countries_dict[alphabet] = c_lst


length_dict = {key: len(value) for key, value in all_countries_dict.items()}


conection_result = {}
for key in (all_countries_dict.keys() | length_dict.keys()):
	if key in all_countries_dict: conection_result.setdefault(key, []).append(all_countries_dict[key])
	if key in length_dict: conection_result.setdefault(key, []).append(length_dict[key])


print(count, len(all_countries))
# print(sorted(all_countries_dict.items()))

# print(sorted(conection_result.items()))

print(all_countries)