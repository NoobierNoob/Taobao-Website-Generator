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

#date stuff
now = datetime.datetime.now()
websites.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

#Amount of times running
howLong1 = input("How many times do you want it to run?")
howLong2 = int(howLong1)
print("Running " + str(howLong2) + " times")
print("Working! Stayed tuned for results")

#variables
siteNumber = 0
successSite = 0


for _ in range(howLong2):
    value = randint(100000000, 999999999)
    #print(value)

    #Total site scanned counter
    siteNumber = siteNumber + 1
    
    success = 0

    #keywords
    words = ['.00', 'palace', 'ader error', 'vlone', 'fog', 'fear of god', 'assc', 'anti', 'drew', 'supreme', '价格', 'cloth', 'fabric', 'clothing', '¥', '物流', 'kanye', '抽绳', '潮牌', '描述']
    
    #future keyword plans here??????
    # keywords = open('./keywords.txt', "a+")
    # keywords.write(str(words))

    #Gets link + puts together
    shop = 'https://shop'
    taobao = '.taobao.com'
    testLink = 'https://nickrosen.city/sadfasdf'
    link = shop + str(value) + taobao

    #searcher
    try:
        site = urllib.request.urlopen(link).read().decode('GBK', errors = 'ignore')
    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        print('URLError: {}'.format(e.reason))
    else:
        for word in words:
          if word in site:
             print(siteNumber, word, link)
             success = 1
    print("Site " + str(siteNumber) + " scanned")

     #txt file stuff
    if success == 1:
        websites.write(str(link) + "\n")
        successSite = successSite + 1
        
print("Complete! Successfully found: " + str(successSite) + " websites with the keywords. Check websites.txt to see them.")

#If results 0 write check
if successSite == 0:
    websites.write('No websites found during session')

websites.write("\n")
os.system("pause")
