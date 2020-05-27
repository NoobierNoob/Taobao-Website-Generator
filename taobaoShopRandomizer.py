import sys
import os
import os.path
import datetime
from random import randint
from urllib.request import urlopen
import urllib.request

#random stuff
print("Welcome, this is Uzi#6900's basic Taobao website generator. \n It was made using python. When prompted, please state how many websites you want it to generate and check for keywords. \nAll websites with said keywords will be placed in websites.txt file that will generate. False positives may occur.")
websites = open('./websites.txt', "a+")

#Amount of times running
howLong1 = input("How many times do you want it to run?")
howLong2 = int(howLong1)
print("Running " + str(howLong2) + " times")
print("Working! Stayed tuned for results")

#variables
siteNumber = 0
successSite = 0

#date stuff
now = datetime.datetime.now()
websites.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

for _ in range(howLong2):
    value = randint(100000000, 999999999)
    #print(value)

    #Total site scanned counter
    siteNumber = siteNumber + 1
    
    #keywords
    words = ['.00', 'palace', 'ader error', 'vlone', 'fog', 'fear of god', 'assc', 'anti', 'drew', 'supreme', '价格', 'cloth', 'fabric', 'clothing', '¥', '物流', 'kanye', '抽绳', '潮牌', '描述']
    
    #future keyword plans here??????
    # keywords = open('./keywords.txt', "a+")
    # keywords.write(str(words))

    #Gets link + puts together
    shop = 'https://shop'
    taobao = '.taobao.com'
    testLink = 'https://shop112744646.taobao.com/'
    link = shop + str(value) + taobao

    #searcher
    site = urllib.request.urlopen(link).read().decode('GBK', errors = 'ignore')
    for word in words:
        if word in site:
            print(siteNumber, word, link)
    print("Site " + str(siteNumber) + " scanned")

    #txt file stuff
    if word in site:
        websites.write(str(link) + "\n")
        successSite = successSite + 1
print("Complete! Successfully found: " + str(successSite) + " websites with the keywords. Check websites.txt to see them.")
websites.write("\n")
os.system("pause")
