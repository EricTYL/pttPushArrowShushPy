#!/usr/bin/python
# coding=utf-8

# Caculates the number of push, arrow and shush in PTT's article.
# Only works for PTT's article.

import re
import requests
from bs4 import BeautifulSoup

url = raw_input("Please enter the PTT article's url: ")
print "This is what you type in: ", url

def pttUrlIsInvalid( URL ):

    # Initializes vars.
    protocol = "NULL"
    hostName = "NULL"
    bbs      = "NULL"
    pttClass = "NULL"
    article  = "NULL"
    listlen  = 0
    i        = 0

    if re.search("^[efhlnpst]{3,6}://", URL) != None:
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
                print "Url is too long, not a PTT article."

    else:
        temptext = URL.split("/")
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
                print "Url is too long, not a PTT article."

    return (( hostName != "www.ptt.cc" ) | ( bbs != "bbs" ) | ( re.search("^index", article ) != None ))

# End of def: pttUrlIsInvalid(URL)



while pttUrlIsInvalid(url):
    url = raw_input("The url is invalid, please give me a PTT article's url: ")
    print "This is what you type in: ", url



# Added protocol in order to get page with right url.
if re.search("^www", url)!=None:
    url = "https://" + url
    print "Protocol is added, url is: ", url

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

push_num  = 0
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
