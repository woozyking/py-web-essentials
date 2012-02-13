#!/usr/bin/python
# -*- coding: utf-8 -*-
# util.py
# TODO: this needs a lot of cleanup!

import urllib
from sys import stdin
import json
import re

QUOTE_SAFE = ','

def unicode_s( s, src_codec ):
    '''
    unicode_s( s, src_codec ) -> unicode str (<type 'unicode'>)

    Returns the unicode version of the input string.
    '''
    return unicode( s, src_codec ).encode('utf-8')

# TODO: add an ignore list of the keys which have values that are not getting normalized
def norm_url( base_url, api_key=[], **param):
    '''
    Stub doc
    '''
    query_str = '?'
    keys = sorted( param.keys() )

    for kw in keys:
        val = str( param[kw] ).strip()
        # take care non-english languages
        val = unicode_s( val, stdin.encoding )
        query = kw + '=' + urllib.quote_plus( val.lower(), QUOTE_SAFE )
        query_str += query + '&'

    if query_str.endswith('&'):
        query_str = query_str[:-1]

    if len(api_key) is 2:
        query_str += '&' + str(api_key[0]) + '=' + str(api_key[1])

    return base_url + query_str

def open_url( url, params=None ):
    '''
    open_url( url ) -> url handler

    Return the URL handler
    '''
    # TODO: exception handling
    return urllib.urlopen( url, params )

def get_json( handler ):
    return json.load( handler, get_encoding( handler.headers ) )

def get_encoding( header ):
    return header['content-type'].split('charset=')[-1]
