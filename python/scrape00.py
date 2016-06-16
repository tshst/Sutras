# -*- coding: utf-8 -*-

import re, urllib2

res = urllib2.urlopen("http://lolipop.jp")
pattern_title = re.compile('<title>(.*?)</title>')
m = pattern_title.search(res.read())
title = m.group(1)
print title
