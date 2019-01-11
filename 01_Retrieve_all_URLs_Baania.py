# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:13:25 2018

@author: Chris
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pickle as pk
import time
import random
#import os
#os.chdir(r"C:\Users\eviriyakovithya\Documents\GitHub\2019-Q1_Baania_webscraping")
#Select Bangkok, Resale condos
#This block will retrive all urls for each page and save to 'urllist' list.

#the first page has different url pattern, add it to the list first, Total 53413 listings (23-DEC-2018)
urllist = [
'https://baania.com/en/listing?stype=for-sale&ptype=2&province=3781'      
]


#Check the url patterns, last page is page=1484
#https://baania.com/en/listing?page=1483&stype=for-sale&ptype=2&province=3781
#Loop from page 1 to page 1483 (last page), append url into QuotePageList.

for i in range(1,1484):
    url="https://baania.com/en/listing?page="+str(i)+"&stype=for-sale&ptype=2&province=3781"
    urllist.append(url)
print(urllist[-5:])


#This block will retrive the link for all condos that show up in each page saved in 'urllist'.
CondoLinkList = [] 

#Loop in the urllist
for url in urllist:

    print("Current Page is "+ url)
#The webpage is now blocked with server security feature which blocks known spider/bot
#workaround as per below suggestion
#https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    
    Soup = BeautifulSoup(webpage, 'html.parser')

    MainTag = Soup.find('ul', attrs={'data-ls-event': 'scroll'})    
    LinkTags = MainTag.findAll('h3', attrs={'class': 'listing-title'})
    print('Number of house inside this page is ' + str(len(LinkTags)))

    #Loop to get link for each condo in each url
    for LinkTag in LinkTags:
        Link = LinkTag.find('a').get('href') #  keyword to retrieve href from Tag (link for each Condo)
        CondoLinkList.append(Link)
    time.sleep(random.randrange(1,3)) #Add sleep time (randomly)

print('CondoLinkList Completed')

# verify with actual webpage
print(CondoLinkList[0])
print(CondoLinkList[-1])

# check the total # of condos, cross check if it matches with owner site
print(len(CondoLinkList))

#Save the as pickle 
with open('CondoLinkList.pkl', 'wb') as f:
    pk.dump(CondoLinkList, f)