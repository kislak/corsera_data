#!/usr/bin/python
import urllib
import json

for i in range(10):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
    j = json.load(response)

    print type(j['results'])
    for i in j['results']:
        print i['text']
