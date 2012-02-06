'''
Module: gmaps.geocode
Author: oEL
Version: 0.1
Description:
    A python wrapper of the Official Google Maps Geocode API
        https://maps.googleapis.com/maps/api/geocode/{format}?{parameters}
'''

from sys import stdin
import urllib2
import json

API_URL         = "http://maps.google.com/maps/geo?q=%s&output=%s&oe=%s&key=%s"
OUTPUT_FORMAT   = "json" # by default. Otherwise xml
OUTPUT_ENCODE   = "utf8"
API_KEY         = ""

def geo_lookup( address ):
    '''
    Stub python doc
    '''

    # Force UTF-8 and normalize query strings 
    address = address.decode(stdin.encoding).encode('utf-8')
    address = urllib2.quote(address)

    # Prepare URL
    url = API_URL % ( address, OUTPUT_FORMAT, OUTPUT_ENCODE, API_KEY )

    # Open URL and get a stream back
    handler = urllib2.urlopen(url)

    # TODO: HTTP header info for encode and status for graceful warnings

    return json.load( handler )

def reverse_lookup( lng, lat ):
    pass
