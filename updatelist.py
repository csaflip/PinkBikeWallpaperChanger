import requests
from bs4 import BeautifulSoup
import json


def get_links(page_num):  # returns list of links
    url_ = requests.get("https://www.pinkbike.com/photo/podlist/?page=" + str(page_num))
    # print(url.content)

    soup = BeautifulSoup(url_.content, "html5lib")
    # print(soup.prettify())
    links = soup.find_all('span', {'class': 'thumbnail crop-thumbnail'})
    # print(links)

    photourls = []

    for link in links:
        temp = link.img['src']
        print(temp)
        temp2 = temp.split('/')
        temp3 = temp2[3].split('p2pb')
        photonum = temp3[1]
        finalurl = 'http://lp1.pinkbike.org/p0pb' + photonum + "/" + photonum + ".jpg"
        # print(finalurl) #url
        photourls.append(finalurl)

    return photourls


data = {} # data starts with 1

data['url'] = []
photourls = get_links(1)

for x in range(1, 20):
    photourls = get_links(x)
    for url in photourls:
        data['url'].append(url)

with open('links.json', 'w') as f:
    json.dump(data, f)
