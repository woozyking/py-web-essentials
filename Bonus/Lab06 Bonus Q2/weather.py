#!/usr/bin/python
# -*- coding: utf-8 -*-
# weather.py (modified for McMaster Eng 1D04)
'''
Weather.py a small module to wrap google's weather api, and makes it possible to
input simple information (e.g. location) and get a bunch of data about weather
'''

# use the C implementation of xml.etree.ElementTree
from xml.etree import cElementTree as ET
import util

API_URL      = "http://www.google.com/ig/api"

WEATHER_TAG  = 'weather'
INFO_TAG     = 'forecast_information'
CURRENT_TAG  = 'current_conditions'
FORECAST_TAG = 'forecast_conditions'

def get_weather( location, locale='en-US' ):
    '''
    get_weather(Location[,language] ) -> dict

    input location desired as a string, [ and language (optional),default english]
    output Weather information,formatted into a dictionary

    '''
    url = util.norm_url( API_URL, [], weather=location, hl=locale )
    res = util.open_url(url)
    data = res.read()
    header = res.headers
    encoding = util.get_encoding(header)

    res.close()

    data = util.unicode_s( data, encoding )
    element = ET.XML(data)

    return Weather(element).raw()

def element2json(element):
    '''
    element2json ( ElementTree Object ) - > dict

    converts an ElementTree Object into a corresponding dictionary, keeping the same
    node distribution.
    
    '''
    children = element.getchildren()
    result = {}

    for child in children:
        # child.tag gives you the tag name
        # child items gives you a list of tuples
        # hardcoded here to reflect the format:
        #   [ ('data', 'Hamilton, ON') ] from Google Weather
        result[child.tag] = child.items()[0][1]

    return result

class Weather(object):
    # TODO: needs tweaks
    
    def __init__( self, root_element ):
        weather_element = root_element.find(WEATHER_TAG)
        info_element = weather_element.find(INFO_TAG)
        curr_element = weather_element.find(CURRENT_TAG)

        # List of all forecast conditions
        fore_elements = weather_element.findall(FORECAST_TAG)
        
        self.info = element2json(info_element)
        self.curr = element2json(curr_element)
        self.fore = []
        
        for f in fore_elements:
            self.fore.append( element2json(f) )

        self.root = { 'version': 1,
                      WEATHER_TAG: {
                          INFO_TAG: self.info,
                          CURRENT_TAG: self.curr,
                          FORECAST_TAG: self.fore }
                      }

    def raw(self):
        return self.root

    def information(self):
        return self.info

    def current(self):
        return self.curr

    def forecast(self):
        return self.fore
