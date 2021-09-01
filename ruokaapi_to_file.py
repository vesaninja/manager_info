#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import urllib.request

def getjson(url):
	with urllib.request.urlopen(url) as response:
		html = response.read()
	return html.decode()

def fetchfood():
	day = str(datetime.now()).split(' ')[0]
	url = "https://api.ruoka.xyz/" + day
	result = getjson(url)
	restaurants = result['restaurants']
	return result

def main():
	day = str(datetime.now()).split(' ')[0]
	url = "https://api.ruoka.xyz/" + day
	result = getjson(url)
	with open('/home/pi/naytto/db/ruoat.json', 'w') as f:
		f.write(result)

main()
