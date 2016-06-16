# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

res = urllib2.urlopen("http://lolipop.jp")
soup = BeautifulSoup(res.read(), "html5lib")
print soup.title

for link in soup.find_all('a'):
    print(link.get('href'))


