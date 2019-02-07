



from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/List_of_airlines_of_Yemen")
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")

for row in table.find_all("tr")[1:]:

    col = row.find_all("td")
    # import pdb
    # pdb.set_trace()
    print(col[0].contents[0]['title'] + " : " + col[2].contents[0])
    # print("\n")


# # https://en.wikipedia.org/wiki/Lists_of_airlines

# import requests
# from bs4 import BeautifulSoup
# import json
# import re

# url = "https://en.wikipedia.org/wiki/List_of_airlines_of_India"

# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")
# tables = soup.find("table", class_="sortable wikitable toccolours")

# # print(str(tables))
# # print(type(tables))
# # for table in tables.find_all("tr")[1:-1]:
# # 	import pdb
# # 	pdb.set_trace()
# 	# print(table)

# # from xml.etree import ElementTree as ET
# from lxml import etree


# parser = etree.HTMLParser()

# tb_strng = '''

# <table class="sortable wikitable toccolours">
# <tbody><tr>
# <th>Airline
# </th>
# <th>Image
# </th>
# <th><a class="mw-redirect" href="/wiki/IATA" title="IATA">IATA</a>
# </th>
# <th><a class="mw-redirect" href="/wiki/ICAO" title="ICAO">ICAO</a>
# </th>
# <th><a class="mw-redirect" href="/wiki/Airline_call_sign" title="Airline call sign">Call Sign</a>
# </th>
# <th>Commenced
# </th>
# <th>Headquarters
# </th>
# <th>Type
# </th></tr>
# <tr>
# <td><a href="/wiki/Air_India" title="Air India">Air India</a></td>
# <td><a class="image" href="/wiki/File:Air_India,_B787-8_Dreamliner,_VT-ANR_(18185615950).jpg"><img alt="Air India, B787-8 Dreamliner, VT-ANR (18185615950).jpg" data-file-height="2000" data-file-width="3000" decoding="async" height="67" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Air_India%2C_B787-8_Dreamliner%2C_VT-ANR_%2818185615950%29.jpg/100px-Air_India%2C_B787-8_Dreamliner%2C_VT-ANR_%2818185615950%29.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Air_India%2C_B787-8_Dreamliner%2C_VT-ANR_%2818185615950%29.jpg/150px-Air_India%2C_B787-8_Dreamliner%2C_VT-ANR_%2818185615950%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Air_India%2C_B787-8_Dreamliner%2C_VT-ANR_%2818185615950%29.jpg/200px-Air_India%2C_B787-8_Dreamliner%2C_VT-ANR_%2818185615950%29.jpg 2x" width="100"/></a></td>
# <td align="center">AI</td>
# <td align="center">AIC</td>
# <td align="center">AIRINDIA</td>
# <td align="center">1946</td>
# <td align="center"><a href="/wiki/Delhi" title="Delhi">Delhi</a></td>
# <td><a class="mw-redirect" href="/wiki/Flag_Carrier" title="Flag Carrier">Full Service</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Jet_Airways" title="Jet Airways">Jet Airways</a></td>
# <td><a class="image" href="/wiki/File:Boeing_737-8HX,_Jet_Airways_JP6781982.jpg"><img alt="Boeing 737-8HX, Jet Airways JP6781982.jpg" data-file-height="870" data-file-width="1280" decoding="async" height="68" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Boeing_737-8HX%2C_Jet_Airways_JP6781982.jpg/100px-Boeing_737-8HX%2C_Jet_Airways_JP6781982.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Boeing_737-8HX%2C_Jet_Airways_JP6781982.jpg/150px-Boeing_737-8HX%2C_Jet_Airways_JP6781982.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Boeing_737-8HX%2C_Jet_Airways_JP6781982.jpg/200px-Boeing_737-8HX%2C_Jet_Airways_JP6781982.jpg 2x" width="100"/></a></td>
# <td align="center">9W</td>
# <td align="center">JAI</td>
# <td align="center">JET AIRWAYS</td>
# <td align="center">1993</td>
# <td align="center"><a href="/wiki/Mumbai" title="Mumbai">Mumbai</a></td>
# <td><a href="/wiki/Flag_carrier" title="Flag carrier">Full Service</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/IndiGo" title="IndiGo">IndiGo</a></td>
# <td><a class="image" href="/wiki/File:IndiGo_Airbus_A320neo_F-WWDG_(to_VT-ITI)_(28915135713).jpg"><img alt="IndiGo Airbus A320neo F-WWDG (to VT-ITI) (28915135713).jpg" data-file-height="3476" data-file-width="5215" decoding="async" height="67" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4d/IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg/100px-IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4d/IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg/150px-IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4d/IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg/200px-IndiGo_Airbus_A320neo_F-WWDG_%28to_VT-ITI%29_%2828915135713%29.jpg 2x" width="100"/></a></td>
# <td align="center">6E</td>
# <td align="center">IGO</td>
# <td align="center">IFLY</td>
# <td align="center">2006</td>
# <td align="center"><a href="/wiki/Gurgaon" title="Gurgaon">Gurgaon</a></td>
# <td><a href="/wiki/Low-cost_carrier" title="Low-cost carrier"> Low Cost</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/SpiceJet" title="SpiceJet">SpiceJet</a></td>
# <td><a class="image" href="/wiki/File:SpiceJet_Boeing_737-900ER_Vyas-1.jpg"><img alt="SpiceJet Boeing 737-900ER Vyas-1.jpg" data-file-height="682" data-file-width="1024" decoding="async" height="67" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/43/SpiceJet_Boeing_737-900ER_Vyas-1.jpg/100px-SpiceJet_Boeing_737-900ER_Vyas-1.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/43/SpiceJet_Boeing_737-900ER_Vyas-1.jpg/150px-SpiceJet_Boeing_737-900ER_Vyas-1.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/43/SpiceJet_Boeing_737-900ER_Vyas-1.jpg/200px-SpiceJet_Boeing_737-900ER_Vyas-1.jpg 2x" width="100"/></a></td>
# <td align="center">SG</td>
# <td align="center">SEJ</td>
# <td align="center">SPICEJET</td>
# <td align="center">2005</td>
# <td align="center"><a href="/wiki/Gurgaon" title="Gurgaon">Gurgaon</a></td>
# <td><a href="/wiki/Low-cost_carrier" title="Low-cost carrier"> Low Cost</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/GoAir" title="GoAir">GoAir</a></td>
# <td><a class="image" href="/wiki/File:GoAir_Airbus_A320_SDS-2.jpg"><img alt="GoAir Airbus A320 SDS-2.jpg" data-file-height="680" data-file-width="1024" decoding="async" height="66" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d3/GoAir_Airbus_A320_SDS-2.jpg/100px-GoAir_Airbus_A320_SDS-2.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/d3/GoAir_Airbus_A320_SDS-2.jpg/150px-GoAir_Airbus_A320_SDS-2.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/d3/GoAir_Airbus_A320_SDS-2.jpg/200px-GoAir_Airbus_A320_SDS-2.jpg 2x" width="100"/></a></td>
# <td align="center">G8</td>
# <td align="center">GOW</td>
# <td align="center">GOAIR</td>
# <td align="center">2005</td>
# <td align="center"><a href="/wiki/Mumbai" title="Mumbai">Mumbai</a></td>
# <td><a href="/wiki/Low-cost_carrier" title="Low-cost carrier"> Low Cost</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/AirAsia_India" title="AirAsia India">AirAsia India</a></td>
# <td><a class="image" href="/wiki/File:VT-APJ_at_IGIA.jpg"><img alt="VT-APJ at IGIA.jpg" data-file-height="801" data-file-width="1200" decoding="async" height="67" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/VT-APJ_at_IGIA.jpg/100px-VT-APJ_at_IGIA.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/VT-APJ_at_IGIA.jpg/150px-VT-APJ_at_IGIA.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9f/VT-APJ_at_IGIA.jpg/200px-VT-APJ_at_IGIA.jpg 2x" width="100"/></a></td>
# <td align="center">I5</td>
# <td align="center">IAD</td>
# <td align="center">RED KNIGHT</td>
# <td align="center">2014</td>
# <td align="center"><a href="/wiki/Bangalore" title="Bangalore">Bangalore</a></td>
# <td><a href="/wiki/Low-cost_carrier" title="Low-cost carrier"> Low Cost</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Vistara" title="Vistara">Vistara</a></td>
# <td><a class="image" href="/wiki/File:Vistara_Airbus_A320-232_at_Delhi_Airport.jpg"><img alt="Vistara Airbus A320-232 at Delhi Airport.jpg" data-file-height="834" data-file-width="1200" decoding="async" height="70" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Vistara_Airbus_A320-232_at_Delhi_Airport.jpg/100px-Vistara_Airbus_A320-232_at_Delhi_Airport.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Vistara_Airbus_A320-232_at_Delhi_Airport.jpg/150px-Vistara_Airbus_A320-232_at_Delhi_Airport.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Vistara_Airbus_A320-232_at_Delhi_Airport.jpg/200px-Vistara_Airbus_A320-232_at_Delhi_Airport.jpg 2x" width="100"/></a></td>
# <td align="center">UK</td>
# <td align="center">VTI</td>
# <td align="center">VISTARA</td>
# <td align="center">2015</td>
# <td align="center"><a href="/wiki/Gurgaon" title="Gurgaon">Gurgaon</a></td>
# <td><a href="/wiki/Flag_carrier" title="Flag carrier">Full Service</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Air_India_Express" title="Air India Express">Air India Express</a></td>
# <td><a class="image" href="/wiki/File:Air_India_Express_VT-AXU.jpg"><img alt="Air India Express VT-AXU.jpg" data-file-height="683" data-file-width="1024" decoding="async" height="67" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Air_India_Express_VT-AXU.jpg/100px-Air_India_Express_VT-AXU.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Air_India_Express_VT-AXU.jpg/150px-Air_India_Express_VT-AXU.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/59/Air_India_Express_VT-AXU.jpg/200px-Air_India_Express_VT-AXU.jpg 2x" width="100"/></a></td>
# <td align="center">IX</td>
# <td align="center">AXB</td>
# <td align="center">EXPRESS INDIA</td>
# <td align="center">2005</td>
# <td align="center"><a href="/wiki/Kochi" title="Kochi">Kochi</a></td>
# <td><a href="/wiki/Low-cost_carrier" title="Low-cost carrier"> Low Cost</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Alliance_Air_(India)" title="Alliance Air (India)">Alliance Air</a></td>
# <td><a class="image" href="/wiki/File:ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_(16869587331).jpg"><img alt="ATR.72-600 AIR INDIA EXPRESS F-WWEZ 1226 TO VT-AIT 10 02 15 TLS (16869587331).jpg" data-file-height="1951" data-file-width="4238" decoding="async" height="46" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/bf/ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_%2816869587331%29.jpg/100px-ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_%2816869587331%29.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/bf/ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_%2816869587331%29.jpg/150px-ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_%2816869587331%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/bf/ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_%2816869587331%29.jpg/200px-ATR.72-600_AIR_INDIA_EXPRESS_F-WWEZ_1226_TO_VT-AIT_10_02_15_TLS_%2816869587331%29.jpg 2x" width="100"/></a></td>
# <td align="center">9I</td>
# <td align="center">LLR</td>
# <td align="center">ALLIED</td>
# <td align="center">1996</td>
# <td align="center"><a href="/wiki/Delhi" title="Delhi">Delhi</a></td>
# <td><a href="/wiki/Regional_airline" title="Regional airline">Regional</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/TruJet" title="TruJet">TruJet</a></td>
# <td><a class="image" href="/wiki/File:TruJet_VT-TMP_at_Hyderabad,_Sep_2015.jpg"><img alt="TruJet VT-TMP at Hyderabad, Sep 2015.jpg" data-file-height="683" data-file-width="1024" decoding="async" height="67" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/53/TruJet_VT-TMP_at_Hyderabad%2C_Sep_2015.jpg/100px-TruJet_VT-TMP_at_Hyderabad%2C_Sep_2015.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/53/TruJet_VT-TMP_at_Hyderabad%2C_Sep_2015.jpg/150px-TruJet_VT-TMP_at_Hyderabad%2C_Sep_2015.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/53/TruJet_VT-TMP_at_Hyderabad%2C_Sep_2015.jpg/200px-TruJet_VT-TMP_at_Hyderabad%2C_Sep_2015.jpg 2x" width="100"/></a></td>
# <td align="center">2T</td>
# <td align="center">TRJ</td>
# <td align="center">TRUJET</td>
# <td align="center">2015</td>
# <td align="center"><a href="/wiki/Hyderabad" title="Hyderabad">Hyderabad</a></td>
# <td><a href="/wiki/Regional_airline" title="Regional airline"> Regional</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Air_Deccan" title="Air Deccan">Air Deccan</a></td>
# <td><a class="image" href="/wiki/File:Air_Deccan_Beechcraft.jpg"><img alt="Air Deccan Beechcraft.jpg" data-file-height="1102" data-file-width="1470" decoding="async" height="75" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/01/Air_Deccan_Beechcraft.jpg/100px-Air_Deccan_Beechcraft.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/01/Air_Deccan_Beechcraft.jpg/150px-Air_Deccan_Beechcraft.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/01/Air_Deccan_Beechcraft.jpg/200px-Air_Deccan_Beechcraft.jpg 2x" width="100"/></a></td>
# <td align="center">DN</td>
# <td align="center">DKN</td>
# <td align="center">DECCAN</td>
# <td align="center">2017</td>
# <td align="center"><a href="/wiki/Mumbai" title="Mumbai">Mumbai</a></td>
# <td><a href="/wiki/Regional_airline" title="Regional airline"> Regional</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Air_Odisha" title="Air Odisha">Air Odisha</a></td>
# <td><a class="image" href="/wiki/File:Utkela_Air_Odisha.jpg"><img alt="Utkela Air Odisha.jpg" data-file-height="647" data-file-width="724" decoding="async" height="89" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/58/Utkela_Air_Odisha.jpg/100px-Utkela_Air_Odisha.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/58/Utkela_Air_Odisha.jpg/150px-Utkela_Air_Odisha.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/58/Utkela_Air_Odisha.jpg/200px-Utkela_Air_Odisha.jpg 2x" width="100"/></a></td>
# <td align="center">6X</td>
# <td align="center">-</td>
# <td align="center">—</td>
# <td align="center">2012</td>
# <td align="center"><a href="/wiki/Bhubaneswar" title="Bhubaneswar">Bhubaneswar</a></td>
# <td><a href="/wiki/Regional_airline" title="Regional airline"> Regional</a>
# </td></tr>
# <tr>
# <td><a class="new" href="/w/index.php?title=Luwang_Air&amp;action=edit&amp;redlink=1" title="Luwang Air (page does not exist)">Luwang Air</a></td>
# <td></td>
# <td align="center">—</td>
# <td align="center">—</td>
# <td align="center">—</td>
# <td align="center">2018</td>
# <td align="center"><a href="/wiki/Kolkata" title="Kolkata">Kolkata</a></td>
# <td><a href="/wiki/Regional_airline" title="Regional airline"> Regional</a>
# </td></tr>
# <tr>
# <td><a href="/wiki/Zoom_Air" title="Zoom Air">Zoom Air</a></td>
# <td></td>
# <td align="center">ZO</td>
# <td align="center">ZOM</td>
# <td align="center">—</td>
# <td align="center">2013</td>
# <td align="center"><a href="/wiki/Gurgaon" title="Gurgaon">Gurgaon</a></td>
# <td><a href="/wiki/Regional_airline" title="Regional airline"> Regional</a>
# </td></tr></tbody></table>

# '''

# tree = etree.fromstring(tb_strng, parser)
# print(tree)
# results = tree.xpath('//tr')

# # print(results)