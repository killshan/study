#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import random
import time

path = '/Users/shane/Desktop/Python Study'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

url = 'https://zoomgirls.net/latest_wallpapers/page/'

img_url = []

for x in range(2):
    x = x+1
    all_url = url+str(x)
    start_html = requests.get(all_url,headers = header)
    d = random.randint(3,12)
    print(d)
    time.sleep(d)
    soup = BeautifulSoup(start_html.text,'lxml')
    all_a = soup.find('ul',class_='wallpapers').find_all('a')
    l = len(all_a)//2
    z = 0
    for y in range(l):
        a1 = all_a[z]
        z = z+2
        href = a1['href']
        img = href.replace("-wallpapers.html","-1920x1080.jpg")
        name = img.replace("/","")
        img = 'https://zoomgirls.net/download'+img
#        pic = requests.get(img,headers = header)
#        f = open(name,'ab')
#        f.write(pic.content)
#        f.close()
#        d = random.randint(15,30)
#        print(d)
#        time.sleep(d)
        img_url.append(img)
        print(img)

ll = len(img_url)
print(ll)



