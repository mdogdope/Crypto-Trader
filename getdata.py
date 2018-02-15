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
		
	#R: Initialize the object to use Ethereum by default
	def __init__(self):
		self.coin = "BTC"

	#P: Sets coin to the desired coin type
	def setcoin(self, usrcoin):
		self.coin = usrcoin

	#P: Gets the amount current in the trade account
	def getavbal(self):
		_bal = 0
		_all_bal = session.get('https://api.hitbtc.com/api/2/trading/balance').json()
		for _x in _all_bal:
			if _x['currency'] == self.coin:
				_bal = float(_x['available'])
				self._bal = _bal
		return format(_bal, '.8f')
		
	#P: Calculates the total value of the coins in account and returns the avg value
	def getpaid(self):
		_value = 0
		_totalbuy = 0
		_totalsell = 0
		_total = self.gettrans()
		_trades = session.get('https://api.hitbtc.com/api/2/history/trades?symbol=' + self.coin + 'BTC').json()
		for _trades in _trades:
			if (_trades['symbol'] == self.coin + "BTC"):
				if _trades['side'] == "buy":
					_value += (float(_trades['quantity'])*float(_trades['price']))
				elif(_trades['side'] == "sell"):
					_value -= (float(_trades['quantity'])*float(_trades['price']))
		_total += self.amtintrade()
		return format(_value/_total, '.8f')
	
	#R: Gets the total amount deposited and withdrawn from the account
	def gettrans(self):
		_total = 0
		_all_trans = session.get('https://api.hitbtc.com/api/2/account/transactions').json()
		for _all_trans in _all_trans:
			if (_all_trans['currency'] == self.coin):
				if (_all_trans['type'] == "payin"):
					_total += float(_all_trans['amount'])
				elif(_all_trans['type'] == "payout"):
					_total -= float(_all_trans['amount'])
		return _total
	
	#R: Calculates the amount in mid-trade
	def amtintrade(self):
		_trades = session.get('https://api.hitbtc.com/api/2/history/trades?symbol=' + self.coin + 'BTC').json()
		_total = 0
		for _trades in _trades:
			if (_trades['symbol'] == self.coin + "BTC"):
				if _trades['side'] == "buy":
					_total += int(_trades['quantity'])
				elif(_trades['side'] == "sell"):
					_total -= int(_trades['quantity'])
		
		return _total
#
#
#
#
#
#
#