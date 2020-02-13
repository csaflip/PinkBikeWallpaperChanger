import requests
from bs4 import BeautifulSoup
import html5lib
import shutil
import random
import json


def output_img(list_of_links):

    image_link = list_of_links[random.randint(0, len(list_of_links))]
    resp = requests.get(image_link, stream=True)
    local_file = open('local_image.jpg', 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp


def get_links():  #returns list of links
    url = requests.get("https://www.pinkbike.com/photo/podlist/?page=1")
    # print(url.content)

    soup = BeautifulSoup(url.content, "html5lib")
    # print(soup.prettify())
    links = soup.find_all('span', {'class': 'thumbnail crop-thumbnail'})
    # print(links)

    photourls = []

    for link in links:
        temp = link.img['src']
        temp2 = temp.split('/')
        temp3 = temp2[3].split('p2pb')
        photonum = temp3[1]
        finalurl = 'http://lp1.pinkbike.org/p0pb' + photonum + "/" + photonum + ".jpg"
        # print(finalurl) #url
        photourls.append(finalurl)

    return photourls


url_list = get_links()

output_img(url_list)
