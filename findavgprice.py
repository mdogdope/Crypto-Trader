
#This program will get my trade history and calculate the average value I bought the coin at.

import requests
import configparser
import json

#Get keys from file
config = configparser.ConfigParser()
config.sections()
config.read('keys.ini')
public_key = config['KEYS']['Public']
secret = config['KEYS']['Private']

#Connect to API
session = requests.session()
session.auth = (public_key, secret)

#Get trade history for all coins
rawhist = session.get('https://api.hitbtc.com/api/2/history/trades').json()

#Combs through json to find one coins data and save to
data = {}
for rawhist in rawhist:
	if rawhist['symbol'] == 'DSHBTC':
		data = rawhist
