#!/usr/bin/python
# -*- coding: utf-8 -*-
# places.py

from pwe import util

API_URL     = "https://maps.googleapis.com/maps/api/place/search/"
OUT_FORMAT  = "json" # can be xml
API_KEY     = "" # REQUIRED, get one from https://code.google.com/apis/console
# Other Parameters: http://code.google.com/apis/maps/documentation/places/#PlaceSearchRequests

def find_place( **params ):
    '''
    Stub doc
    '''

    # TODO: validate location and radius types and values
    
    url = util.norm_url( API_URL + OUT_FORMAT, ['key', API_KEY], **params )
    res = util.open_url(url)
    j = util.get_json(res)

    res.close()

    return j
