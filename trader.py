import requests
import configparser

#Get keys from file
config = configparser.ConfigParser()
config.sections()
config.read('keys.ini')
public_key = config['KEYS']['Public']
secret = config['KEYS']['Private']

#Sets up api requests
session = requests.session() 

session.auth = (public_key, secret)

##Gets the json file used in software
#Get json for orders
orders = session.get('https://api.hitbtc.com/api/2/order').json()

#Get json for balance
balance = session.get('https://api.hitbtc.com/api/2/trading/balance').json()

#Get json for prices
price = session.get('https://api.hitbtc.com/api/2/public/ticker').json()
print(price)


#Places order
order = {'symbol':'BCNBTC', 'side': 'buy', 'quantity': '0', 'price': '0.0000006416'}
trade = session.post('https://api.hitbtc.com/api/2/order', data = order)
print(trade.json())



#searches json for certian order
for orders in orders:
	if orders['symbol'] == 'DSHBTC':
		order = float(orders['quantity'])
		print (order)

#Searches balance json for the type
for balance in balance:

	if balance['currency'] == 'BTC':
		bal = float(balance['available'])
		print (bal)
		
#Searches price json for the type
for price in price:

	if price['symbol'] == 'DSHBTC':
		price1 = str(price['last'])
		print (price1)
