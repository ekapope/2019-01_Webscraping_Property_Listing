# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:24:30 2018

@author: Chris
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pickle as pk
import time
import numpy as np
import pandas as pd
import random

import os
os.chdir(r"C:\Users\eviriyakovithya\Documents\GitHub\2019-Q1_Baania_webscraping")
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

#load the retrived URL list
with open('CondoLinkList.pkl','rb') as f:  # Python 3: open(..., 'rb')
    (CondoLinkList) = pk.load(f)
#check the length    
len(CondoLinkList)
###############################################################################
#Check each element in the page
url=CondoLinkList[3]
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
Soup = BeautifulSoup(webpage, 'html.parser')

CondoName  = Soup.find('div', attrs={'class': 'title-name'})
if(CondoName!=None): CondoName=CondoName.find('h1').text
else: CondoName=np.nan
print(CondoName)

#RoomDetail (EntityDetail)
EntityDetail = Soup.find('div', attrs={'class': 'entity-detail'})
print(EntityDetail)

SalePrice = EntityDetail.find('div', attrs={'class': 'number-item price selling-price'})
if(SalePrice!=None): SalePrice=int(SalePrice.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: SalePrice=np.nan
print(SalePrice)

RentPrice = EntityDetail.find('div', attrs={'class': 'number-item price renting-price'})
if(RentPrice!=None): RentPrice=int(RentPrice.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: RentPrice=np.nan
print(RentPrice)

RoomArea = EntityDetail.find('div', attrs={'class': 'number-item usable-area'})
if(RoomArea!=None): RoomArea=int(RoomArea.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: RoomArea=np.nan
print(RoomArea)

UnitNbr = EntityDetail.find('div', attrs={'class': 'number-item unit-number'})
if(UnitNbr!=None): UnitNbr=str(UnitNbr.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: UnitNbr=np.nan
print(UnitNbr)

FloorNbr = EntityDetail.find('div', attrs={'class': 'number-item at-floor'})
if(FloorNbr!=None): FloorNbr=str(FloorNbr.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: FloorNbr=np.nan
print(FloorNbr)

nbrBed = EntityDetail.find('div', attrs={'class': 'number-item bed'})
if(nbrBed!=None): nbrBed=str(nbrBed.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: nbrBed=np.nan
print(nbrBed)

nbrBath = EntityDetail.find('div', attrs={'class': 'number-item bath'})
if(nbrBath!=None): nbrBath=str(nbrBath.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: nbrBath=np.nan
print(nbrBath)

nbrPark = EntityDetail.find('div', attrs={'class': 'number-item parking'})
if(nbrPark!=None): nbrPark=str(nbrPark.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: nbrPark=np.nan
print(nbrPark)

nbrAirCon = EntityDetail.find('div', attrs={'class': 'number-item aircond'})
if(nbrAirCon!=None): nbrAirCon=str(nbrAirCon.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',',''))
else: nbrAirCon=np.nan
print(nbrAirCon)

LatLong = EntityDetail.find('div', attrs={'class': 'location-item latlong'})
if(LatLong!=None): 
    Latitude,Longitude =LatLong.find('div', attrs={'class': 'value'}).text.split(',')
    Latitude=float(Latitude)
    Longitude=float(Longitude)
else:
    Latitude = np.nan
    Longitude = np.nan
print(Latitude,Longitude)
###############################################################################
#Put the code above into function
#Write function to retrive room info for each page
def func_Scrape_RoomInfo(QuotePage):

    req = Request(QuotePage, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    Soup = BeautifulSoup(webpage, 'html.parser')
    
    CondoName  = Soup.find('div', attrs={'class': 'title-name'})
    if(CondoName!=None): CondoName=CondoName.find('h1').text
    else: CondoName=np.nan
#    print(CondoName)
    
    #RoomDetail (EntityDetail)
    EntityDetail = Soup.find('div', attrs={'class': 'entity-detail'})
#    print(EntityDetail)
    
    SalePrice = EntityDetail.find('div', attrs={'class': 'number-item price selling-price'})
    if(SalePrice!=None): SalePrice=str(SalePrice.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: SalePrice=np.nan
    print(SalePrice)
    
    RentPrice = EntityDetail.find('div', attrs={'class': 'number-item price renting-price'})
    if(RentPrice!=None): RentPrice=str(RentPrice.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: RentPrice=np.nan
    print(RentPrice)
    
    RoomArea = EntityDetail.find('div', attrs={'class': 'number-item usable-area'})
    if(RoomArea!=None): RoomArea=str(RoomArea.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: RoomArea=np.nan
    print(RoomArea)
    
    UnitNbr = EntityDetail.find('div', attrs={'class': 'number-item unit-number'})
    if(UnitNbr!=None): UnitNbr=str(UnitNbr.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: UnitNbr=np.nan
    print(UnitNbr)
    
    FloorNbr = EntityDetail.find('div', attrs={'class': 'number-item at-floor'})
    if(FloorNbr!=None): FloorNbr=str(FloorNbr.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: FloorNbr=np.nan
    print(FloorNbr)
    
    nbrBed = EntityDetail.find('div', attrs={'class': 'number-item bed'})
    if(nbrBed!=None): nbrBed=str(nbrBed.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: nbrBed=np.nan
    print(nbrBed)
    
    nbrBath = EntityDetail.find('div', attrs={'class': 'number-item bath'})
    if(nbrBath!=None): nbrBath=str(nbrBath.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: nbrBath=np.nan
    print(nbrBath)
    
    nbrPark = EntityDetail.find('div', attrs={'class': 'number-item parking'})
    if(nbrPark!=None): nbrPark=str(nbrPark.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: nbrPark=np.nan
    print(nbrPark)
    
    nbrAirCon = EntityDetail.find('div', attrs={'class': 'number-item aircond'})
    if(nbrAirCon!=None): nbrAirCon=str(nbrAirCon.find('div', attrs={'class': 'value'}).text.split(' ')[0].replace(',','').strip())
    else: nbrAirCon=np.nan
    print(nbrAirCon)
    
    LatLong = EntityDetail.find('div', attrs={'class': 'location-item latlong'})
    if(LatLong!=None): 
        Latitude,Longitude =LatLong.find('div', attrs={'class': 'value'}).text.split(',')
        Latitude=float(Latitude)
        Longitude=float(Longitude)
    else:
        Latitude = np.nan
        Longitude = np.nan
    print(Latitude,Longitude)
    
    roominfo= (CondoName,SalePrice,RentPrice,RoomArea,UnitNbr,FloorNbr,nbrBed,nbrBath,nbrPark,nbrAirCon,Latitude,Longitude)
       
    return roominfo
###############################################################################
#function to define time format
#https://arcpy.wordpress.com/2012/04/20/146/
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60.
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)
##############################################################################
#Retrive info for each page, using for loop, save as dataframe and csv
colnames=['CondoName','SalePrice','RentPrice','RoomArea',
          'UnitNbr','FloorNbr','nbrBed','nbrBath','nbrPark','nbrAirCon',
          'Latitude','Longitude']
all_rooms_df = pd.DataFrame(columns=colnames)
start_time=time.time()
for i in range(50001,len(CondoLinkList)):
    try:
        current_room = func_Scrape_RoomInfo(CondoLinkList[i])
        all_rooms_df = all_rooms_df.append(pd.DataFrame([current_room], columns=colnames),ignore_index=True)
        print('-------------- Completed Condo # '+str(i)+"/"+str(len(CondoLinkList)))
        print("Total time {} ".format(hms_string(time.time() - start_time)))
        time.sleep(random.randrange(1,3))    #Add sleep time 1-3 secs
        if(i!=0 and i%1000==0): # save to csv every 1000 rows and clear df for next loop
            all_rooms_df.to_csv('./all_rooms_df'+str(i)+'.csv', header=True, sep=',',index=False, encoding='utf-8-sig')
            all_rooms_df = pd.DataFrame(columns=colnames)
        next
    except:
        next
all_rooms_df.to_csv('./all_rooms_df_last.csv', header=True, sep=',',index=False, encoding='utf-8-sig')
print('---------------- Scraping Completed ----------------')
print("Total time {} ".format(hms_string(time.time() - start_time)))
###############################################################################