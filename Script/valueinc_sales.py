# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:24:39 2023

@author: franc
"""

import pandas as pd

# file_name = pd.read_scv('file.csv') <---- format of read_csv

data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv',sep=';')

# summary of the data
data.info()

# Working with calculations
# Defining variables

CostPerItem = 11.73
SellingPricePerItem= 21.11
NumberofItemsPurchased= 6

# Mathematical operations on Phyton

ProfitPerItem = 21.11 - 11.73
profitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

# CostPerTransaction Column Calculation

# CostPerTransaction = CostPerItem * NumberofItemsPurchased

# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

# Adding a new colomn to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost)/Cost

data['Markup'] = (data['ProfitperTransaction'])/data['CostPerTransaction']

# Rounding Marking

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

# Combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

# Checking columns data type

print(data['Day'].dtype)

# Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day+'-'+data['Month']+'-'+year
print(day.dtype)

data['Date'] =my_date

# Using iloc to view specific columns/row

data.iloc[0] #views the wrow with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows
data.iloc[:,2]

data.iloc[4,2] #brings in all rows on the 2nd column

# Using split to split the client keywords field

#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

# Creating new columns for the split columns in client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LenghtofContract'] = split_col[2]

# Using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LenghtofContract'] = data['LenghtofContract'].str.replace(']' , '')

# Using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

# How to merge files

# Bringing in a new dataset

season = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, season, on = 'Month')

# Dropping columns

# df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop(['Year','Month'], axis=1)

# Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)