#!/usr/bin/python
# coding=utf-8

# Caculates the number of push, arrow and shush in PTT's article.
# Only works for PTT's article.

# Works fine in Python 2.7.6
# You should have installed the given version of packages:
#
# 1.beautifulsoup4  4.4.0
# 2.requests        2.7.0

import re
import requests
from bs4 import BeautifulSoup

url = raw_input("Please enter the PTT article's url: ")
print "This is what you type in: ", url

def pttUrlIsInvalid( uRL ):

    # Initializes vars.
    i        = 0
    protocol = "Null"
    hostName = "NULL"
    bbs      = "NULL"
    pttClass = "NULL"
    article  = "NULL"
    print "type of ", uRL, " : ", type(uRL), "\n"
    URL = uRL
    listlen = 0
    i       = 0
    if re.search("^[efhlnpst]{3,6}://", URL) != None:
        print "In if \n"
        temptext = URL.split("://")
        protocol = temptext[0]
        listlen  = len(temptext[1].split("/"))
        while i < listlen:
            i += 1
            if   i == 1:
                hostName = temptext[1].split("/")[0]
            elif i == 2:
                bbs      = temptext[1].split("/")[1]
            elif i == 3:
                pttClass = temptext[1].split("/")[2]
            elif i == 4:
                article  = temptext[1].split("/")[3]
            else:
                print "Out of list, or not a PTT article's url."
    else:
        print "In else \n"
        temptext = URL.split("/")
        protocol = "https"
        listlen  = len(temptext)
        while i < listlen:
            i += 1
            if   i == 1:
                hostName = temptext[0]
            elif i == 2:
                bbs      = temptext[1]
            elif i == 3:
                pttClass = temptext[2]
            elif i == 4:
                article  = temptext[3]
            else:
                print "Out of list, or not a PTT article's url."
    
    print protocol, "\n", hostName, "\n", bbs, "\n", pttClass, "\n", article, "\n"
    return (( hostName != "www.ptt.cc" ) | ( bbs != "bbs" ) | ( re.search("^index", article ) != None ))

while pttUrlIsInvalid(url):
    print "In invalid while."
    url = raw_input("The url is invalid, please give me a PTT article's url: ")
    print "This is what you type in: ", url

print re.search("", url)
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

push_num = 0
arrow_num = 0
shush_num = 0

for entry in soup.select('.push'):

    if entry.select('.push-tag')[0].text == u"推 ":
        push_num += 1
    elif entry.select('.push-tag')[0].text == u"噓 ":
        shush_num += 1
    else:
        arrow_num += 1

print "push: ", push_num, "\n", "arrow: ", arrow_num, "\n", "shush: ", shush_num, "\n"

#print res.text
