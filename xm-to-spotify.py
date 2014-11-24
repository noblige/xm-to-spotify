#!/usr/bin/python

from httplib2 import Http
from BeautifulSoup import BeautifulSoup
import json, urllib

client = Http()

resp, data = client.request('http://www.dogstarradio.com/search_playlist.php?artist=&title=&channel=264&month=&date=&shour=&sampm=&stz=&ehour=&eampm=')

html = BeautifulSoup(data)

for s in html('table')[1]('tr')[3:]:
	r = s('td')
	a, n = r[1].text, r[2].text
	r, d = client.request('https://api.spotify.com/v1/search?market=us&type=track&q=' + urllib.quote(n + ' ' + a))
	data = json.loads(d)
	if not data['tracks']['items']:
		continue
	sa, sn = data['tracks']['items'][0]['artists'][0]['name'], data['tracks']['items'][0]['name']
	print data['tracks']['items'][0]['uri'], '\t', sa, '-', sn
