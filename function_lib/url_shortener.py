#!/usr/bin/python
# -*- coding: utf-8 -*-
# url_shortener.py

import json
import urllib2

API_URL = 'https://www.googleapis.com/urlshortener/v1/url'

def shorten( url, output='json', charset='utf-8' ):
    '''
    shorten( url, output='json', charset='utf-8' ) -> JSON <type 'dict'>

    Takes an url to be shortened and returns JSON feedback <type 'dict'>.

    Sample usage:
    >>> j = shorten( 'http://google.com' ) # http:// or https:// is optional
    >>> print j['id'] # the id field gives you the shortened url
    http://goo.gl/mR2d
    '''
    headers = {
        'Content-Type': 'application/'+output,
        'charset': charset
        }

    data = json.dumps( {'longUrl': url} )
    req = urllib2.Request( API_URL, data, headers )
    res = urllib2.urlopen(req)
    j = json.load(res)

    res.close()

    return j
    
def expand( short_url ):
    '''
    expand( short_url ) -> JSON <type 'dict'>

    Takes an shortened url from goo.gl and returns JSON feedback <type 'dict'>

    Notice that it only works for goo.gl short urls.

    Sample usage:
    >>> j = expand( 'goo.gl/mR2d' ) # http:// or https:// is optional
    >>> print j['longUrl']
    http://google.com/
    '''
    if not (short_url.startswith('http://') or short_url.startswith('https://')):
        short_url = 'http://' + short_url

    url = API_URL + '?shortUrl=' + short_url
    res = urllib2.urlopen(url)
    j = json.load(res)

    res.close()

    return j
