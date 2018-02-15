from getdata import TotalCost
import requests
import configparser
import json


x = TotalCost()
x.setcoin("DSH")
print (x.getpaid())
#print(x.getbal())
'''
config = configparser.ConfigParser()
config.sections()
config.read('keys.ini')
public_key = config['KEYS']['Public']
secret = config['KEYS']['Private']


session = requests.session() 
session.auth = (public_key, secret)

_trades = session.get('https://api.hitbtc.com/api/2/history/trades?symbol=DSHBTC').json()

for _trades in _trades:
	if (_trades['symbol'] == "DSHBTC"):
		print(_trades['quantity'])
'''