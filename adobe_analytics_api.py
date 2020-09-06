#import adobe analytics and standard python libraries(if you do not have adobe analytics already installed, please install them using pip install command from command prompt)

import adobe_analytics
from adobe_analytics import Client, ReportDefinition
from adobe_analytics import download_async
import pandas as pd
from datetime import date
from datetime import timedelta

#Create dymanic datetime range for automation purpose (you may ignore this step , if you want the date rnage to static)

today = date.today()
d1 = str(date(today.year,today.month,today.day) - timedelta(days=7))
d2 = str(date(today.year,today.month,today.day) - timedelta(days=1))
d3 = str(date(today.year,today.month,today.day))

# Authenticate your access to adobe analytics API using unique key ( Ask you Adobe administrator to provide you the unique key against your account) 
# organisation name is the name of organisation as per adobe analytics

client = Client('email.address@company.com:Organisation Name', 'unique Key')

# Remeber, Adobe Analytics takes every aurgument as IDs , not their actual names as per workspace so it is important to know the ID's of all dimentions, segemnts, report suites.

# get the list of report suites with ID's available in organisation and save them to csv file for future references 
 
d = client.suites()
df1=pd.DataFrame.from_dict(d,orient='index')
df1.to_csv("path"+'.csv',index=True)

# Get the Dimentions of specific report suite 

suite = client.suites()['Suite-ID']

seg=suite.dimensions()
df2=pd.DataFrame.from_dict(seg,orient='index')
df2.head()
df2.to_csv("Path"+"dimentions-suite1"+'.csv',index=False)

# Get the Segments of specific report suite 

suite = client.suites()['Suite-ID']

seg=suite.Segments()
df2=pd.DataFrame.from_dict(seg,orient='index')
df2.head()
df2.to_csv("Path"+"Segments-suite1"+'.csv',index=False)

#Now you know the ID's of dimentions, segments and suites, you can start API call for data by providing different parameters.
# download_async method gives us the flexbility to download the same report from multiple report suite at once 
# top = number of rows to be pulled for specific dimention
# You can change how date_from and date_to is called

report_def = ReportDefinition(metrics=['visits','Orders'],
                              dimensions=[{"id":"dimention_id","top": 500}],
                              segemnts=[{"id":"segment1-id"},{"id":"segment2-id"},{"id":"segment3-id"},{"id":"segment4-id"}],
                              date_from= str(date(today.year,today.month,today.day) - timedelta(days=1)),
                              date_to= str(date(today.year,today.month,today.day)),
                              granularity='hour')
adobe_data = download_async(client, report_def, suite_ids=["suite-1","suite-2", "suite-3"])

# well done , Now you have a data frame in python with adobe analytics data in it. you can utilize this in multiple ways.
#Thank You
