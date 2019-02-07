import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import re
import urllib.request
# from BeautifulSoup import BeautifulSoup, 

url = "https://en.wikipedia.org/wiki/Lists_of_airlines"
# response = requests.get(url)

# soup = BeautifulSoup(response.text)



new_url = urllib.request.urlopen(url).read()

ALL_CONTINENT = ["Asia", "Africa", "Europe", "America", "Oceania", "Antarctica"]
continent_airline_link = []
soup = BeautifulSoup(new_url)
for line in soup.find_all('a'):
	# import pdb
	# pdb.set_trace()
	title = line.get('title')
	if title:
		for conti in ALL_CONTINENT:
			check = title.__contains__(conti)
			if check:
				continent_airline_link.append(line)
				# print(line)
		

# print(continent_airline_link)
continet_list_airline = []

for con in continent_airline_link:
	con_lst =  con.attrs['href'].__contains__("List")
	if con_lst:
		continet_list_airline.append(con.attrs['href'])


print(continet_list_airline)



# import httplib2
# # from BeautifulSoup import BeautifulSoup, SoupStrainer



# for each_country in continet_list_airline:
# 	new_url = "https://en.wikipedia.org" + str(each_country)
# 	# soup = BeautifulSoup(new_url)
# 	# for line in soup.find_all('a'):
# 	# 	print(line)


# 	http = httplib2.Http()
# 	status, response = http.request(new_url)


# 	for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
# 		import pdb
# 		pdb.set_trace()
# 		if link.has_attr('href'):
# 			print(link['href'])


# from urllib.request import urlopen
# from bs4 import BeautifulSoup


# html = urlopen("https://en.wikipedia.org/wiki/List_of_airlines_of_India")
# soup = BeautifulSoup(html, "html.parser")
# table = soup.find("table")

# for row in table.find_all("tr")[1:]:

#     col = row.find_all("td")
#     # import pdb
#     # pdb.set_trace()
#     print(col[0].contents[0]['title'] + " : " + col[2].contents[0])
    # print("\n")

