import sys
import os
import os.path
import datetime
from random import randint
from urllib.request import urlopen
import urllib.request
from colorama import init, Fore, Back, Style
from time import sleep
init(autoreset=True)

#random stuff
print(Fore.CYAN + "Welcome, this is Uzi#6900's basic Taobao website generator.")
print("It was made using python. When prompted, please state how many websites you want it to generate and check for keywords.\nAll websites with said keywords will be placed in websites.txt file that will generate.")
print(Fore.YELLOW + Style.BRIGHT + "Edit keywords in keywords.txt")
print(Fore.RED + Style.BRIGHT + "False positives may occur.")
websites = open('./websites.txt', "a+")

#date stuff
now = datetime.datetime.now()
websites.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

#Amount of times running
howLong1 = int(input("How many times do you want it to run?"))
print("Running " + str(howLong1) + " times")
print("Working! Stayed tuned for results")

#variables
siteNumber = 0
successSite = 0

#keywords
words = ['.00', '价格', '物流', '抽绳', '潮牌', '描述']

try:
    with open('./keywords.txt', "x", encoding="utf-8") as g:
        g.write('.00\n' '价格\n' '物流\n' '抽绳\n' '潮牌\n' '描述\n')
except FileExistsError:
    print('Reading keywords')
    with open('./keywords.txt' , "r", encoding="utf-8") as myFile:
        words = myFile.read().splitlines()
        print(words)

#Looper
for _ in range(howLong1):
    value = randint(100000000, 999999999)
    #print(value)

    #Total site scanned counter
    siteNumber = siteNumber + 1
    if siteNumber >= 500:
        sleep(5)
    success = 0


    #Gets link + puts together
    shop = 'https://shop'
    taobao = '.taobao.com'
    testLink = 'https://shop62698926.taobao.com/.'
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
             print(siteNumber, word, Fore.LIGHTRED_EX + link)
             success = 1
    print("Site " + str(siteNumber) + " scanned")

     #txt file stuff
    if success == 1:
        websites.write(str(link) + "\n")
        successSite = successSite + 1
        
print(Fore.GREEN + Style.BRIGHT + "Complete! Successfully found: " + str(successSite) + " websites with the keywords. Check websites.txt to see them.")

#If results 0 write check
if successSite == 0:
    websites.write('No websites found during session')

websites.write("\n")
os.system("pause")
