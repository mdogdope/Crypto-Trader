import configparser

config = configparser.ConfigParser()

config['KEYS'] = {'Public':'Your HitBtc public key here', 'Private':'Your HitBtc private key here'}

with open('keys.ini', 'w') as configfile:
	config.write(configfile)
