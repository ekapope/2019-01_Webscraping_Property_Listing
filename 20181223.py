# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:13:25 2018

@author: Chris
"""

import urllib
from bs4 import BeautifulSoup
import pickle as pk

#Select Bangkok, Resale condos
#This block will retrive all urls for each page and save to 'urllist' list.

#Add url of the first page
urllist = [
'https://baania.com/en/projects?ptype=2&province=3781&stype=resale-project'      
]

#Check the url patterns, last page is page=67
#Loop from page 1 to page 67 (last page), append url into QuotePageList.
#Resale Projects Total 1202 projects

for i in range(1,68):
    url="https://baania.com/en/projects?page="+str(i)+"&ptype=2&province=3781&stype=resale-project"
    urllist.append(url)
print(urllist[-5:])

import time

#This block will retrive the link for all condos that show up in each page saved in 'urllist'.

CondoLinkList = [] 

#Loop in the urllist
for url in urllist:

    print("Current Page is "+ url)
    
    Page = urllib.request.urlopen(url)
    Soup = BeautifulSoup(Page, 'html.parser')

    MainTag = Soup.find('ul', attrs={'data-ls-event': 'scroll'})    
    LinkTags = MainTag.findAll('h3', attrs={'class': 'header-title'})
    print('Number of house inside this page is ' + str(len(LinkTags)))

    #Loop to get link for each condo in each url
    for LinkTag in LinkTags:
        Link = LinkTag.find('a').get('href') # อันนี้คือ keyword ของการดึง href จาก Tag (link ของแต่ละ Condo)
        CondoLinkList.append(Link)
    time.sleep(3) #Add sleep time (3 sec)

print('CondoLinkList Completed')

# verify with actual webpage
print(CondoLinkList[0])
print(CondoLinkList[-1])

# check the total # of condos, cross check if it matches with owner site
print(len(CondoLinkList))

#Save the as pickle 
with open('CondoLinkList.pkl', 'wb') as f:
    pk.dump(CondoLinkList, f)