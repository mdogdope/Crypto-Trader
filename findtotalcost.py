#This file holds the functions that will get the trade history, calculate the total price, and will return the info.

import requests
import configparser
import json

class TotalCost:
	#Get keys from file
	config = configparser.ConfigParser()
	config.sections()
	config.read('keys.ini')
	public_key = config['KEYS']['Public']
	secret = config['KEYS']['Private']

	#Sets up api requests
	global session
	session = requests.session() 
	session.auth = (public_key, secret)
		
	#Initialize the object to use Ethereum by default
	def __init__(self):
		self.coin = "BTC"

	#Sets coin to the desired coin type
	def setcoin(self, usrcoin):
		self.coin = usrcoin

	def getbal(self):
		_bal = 0
		_all_bal = session.get('https://api.hitbtc.com/api/2/trading/balance').json()
		for _x in _all_bal:
			if _x['currency'] == self.coin:
				_bal = float(_x['available'])
				self._bal = _bal
		return format(_bal, '.8f')
	def getvalue(self):
		
		
		
		
		
		
		
		