    '''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal


userChoices = queries()

                if ( userChoices[2] == 1 ):
                    payload = {'function':'TIME_SERIES_INTRADAY' , 'symbol':userChoices[0], 'interval':'30min' , 'apikey' :'P8HT9FLVF2HF2HZB'}
                    nestedName = "Time Series (30min)"
                    
                elif( userChoices[2] == 2):
                    payload = {'function':'TIME_SERIES_DAILY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
                    nestedName = "Time Series (Daily)"
                    
                elif( userChoices[2] == 3 ):
                    payload = {'function':'TIME_SERIES_WEEKLY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
                    nestedName = "Time Series (Weekly)"
                    
                else:
                    payload = {'function':'TIME_SERIES_MONTHLY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
                    nestedName = "Time Series (Monthly)"
                    

results = requests.get('https://www.alphavantage.co/query', params=payload)

import requests
from datetime import datetime
from datetime import date
import pygal

#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()
