from getdata import TotalCost
import requests
import configparser
import json


x = TotalCost()
x.setcoin("DSH")
print (x.getpaid())
print(x.getbal())
