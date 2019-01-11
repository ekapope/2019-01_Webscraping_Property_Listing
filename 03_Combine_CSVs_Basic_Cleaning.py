# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:17:44 2019

@author: eviriyakovithya
"""

#find all csv files in the folder
import glob
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
import pandas as pd
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# how many NaN in each columns?
print(combined_csv.info())
print(combined_csv.isna().sum()/len(combined_csv)*100)

# drop missing rows for Latitude and Longitude
combined_csv=combined_csv.dropna(subset=['Latitude', 'Longitude','SalePrice','RoomArea'])

# add 'SalePrice_per_sqm' column
combined_csv['SalePrice_per_sqm'] = combined_csv['SalePrice']/combined_csv['RoomArea']

# export to csv
combined_csv.to_csv( "combined_csv.csv", index=False,encoding='utf-8-sig')