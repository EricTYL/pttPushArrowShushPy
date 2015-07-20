#!/usr/bin/python
# coding=utf-8

# Caculates the number of push, arrow and shush in PTT's article.
# Only works for PTT's article.

# Works fine in Python 2.7.6
# You should have installed the given version of packages:
#
# 1.beautifulsoup4  4.4.0
# 2.requests        2.7.0

import requests
from bs4 import BeautifulSoup

url = raw_input("Please enter the PTT article's url: ")
print "This is what you type in: ", url 
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

num = 0
push_num = 0
arrow_num = 0
shush_num = 0
for entry in soup.select('.push'):
    num += 1

    if entry.select('.push-tag')[0].text == u"推 ":
        push_num += 1
    elif entry.select('.push-tag')[0].text == u"噓 ":
        shush_num += 1
    else:
        arrow_num += 1

print "push: ", push_num, "\n", "arrow: ", arrow_num, "\n", "shush: ", shush_num, "\n"


