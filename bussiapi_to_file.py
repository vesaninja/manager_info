#!/usr/bin/env python3

import urllib.request
def getjson(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html.decode()

def readConfig(filename):
    optiondict = {}
    with open(filename, 'r') as configfile:
        for row in configfile:
            options = row.split(' = ')
            options[1] = options[1].replace("\n", "")
            optiondict[options[0]] = options[1]
    return optiondict

def main():
    stop = 3735
    linjojenmaara = 5
    options = readConfig("/home/pi/naytto/options/busapi.conf")
    url = "http://api.publictransport.tampere.fi/prod/?request=stop&user=" + options["user"] + "&pass=" + options["password"] + "&code=" + str(stop) + "&dep_limit=" + str(linjojenmaara)
    result = getjson(url)
    with open('./db/bussit.json', 'w') as f:
        f.write(result)

main()
