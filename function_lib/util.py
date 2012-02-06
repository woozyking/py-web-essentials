# util.py

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

def norm_url( base_url, **param ):
    '''
    Stub doc
    '''
    if base_url.endswith('/'):
        base_url = base_url[:-1]

    if not base_url.endswith('?'):
        query_str = '?'
    else:
        query_str = ''
    
    if not param.has_key('sensor'):
        param['sensor'] = 'false'
    
    keys = sorted( param.keys() )

    for kw in keys:
        val = str( param[kw] ).strip()
        val = unicode_s( val, stdin.encoding )
        query = kw + '=' + urllib.quote_plus( val, QUOTE_SAFE )
        query_str += query + '&'

    if query_str.endswith('&'):
        query_str = query_str[:-1]

    return (base_url + query_str).lower()

def open_url( url ):
    '''
    open_url( url ) -> url handler

    Return the URL handler
    '''
    handler = None
    
    try:
        handler = urllib.urlopen( url )
    except urllib.URLError:
        # TODO: exception handling
        pass

    return handler

def get_json( handler ):
    j = json.load( handler, get_encoding( get_headers(handler) ) )
    
    return j

def get_headers( handler ):
    return handler.headers

def get_encoding( header ):
    return header['content-type'].split('charset=')[-1]
