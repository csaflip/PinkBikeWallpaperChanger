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


def get_links_from_json():  #returns list of links
    with open('links.json') as f:
        data = json.load(f)
    outdata = data['url']

    return outdata


url_list = get_links_from_json()

output_img(url_list)
