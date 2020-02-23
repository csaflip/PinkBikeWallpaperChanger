import requests
from bs4 import BeautifulSoup
import html5lib
import shutil
import random
import json
import subprocess
from datetime import datetime
import sys
import ctypes
import os

random.seed(datetime.now())


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


SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""


def set_desktop_background(filename):
    if sys.platform.startswith('win32'):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filename, 3)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(SCRIPT % filename, shell=True)
        subprocess.call(["killall Dock"], shell=True)



url_list = get_links_from_json()

output_img(url_list)

set_desktop_background(os.getcwd() + 'local_image.jpg')
