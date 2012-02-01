'''
Module: py-web-essentials.function_lib.weather (TODO: proper packages)
Author: oEL
Version: 0.5
Description:
    A python wrapper of the unofficial Google Weather API:
        http://www.google.com/ig/api?weather={location}&hl={locale}
    Handles different languages properly
Known issues: none
TODO & FIXME: see in-line comments
'''

from sys import stdin
import urllib2
from xml.dom import minidom

API_URL = "http://www.google.com/ig/api?weather=%s&hl=%s"

def get_weather( location, locale='' ):
    '''
    get_weather( location[, locale] ) ->
        DOM Object that contains weather info
        or "ERROR" if something's wrong (for now, FIXME)
    
    location - (case insensitive) a location string, possible cases are:
        * Specific landmark, e.g. McMaster University
        * Longitude, Lantitude
        * Postal code
        * City name, [province/state], [country], e.g. Hamilton, ON, Canada
            **  Province/state and country are optional,
            **  Though you might get an unwanted city
    locale - (case insensitive) [optional], output language, see:
        https://sites.google.com/site/tomihasa/google-language-codes

    Sample usage:
    >>> dom_obj = get_weather( 'McMaster University', 'en-US' )
    >>> xml_str = dom_obj.toprettyxml()
    >>> print xml_str
    ...
    '''

    # Make location in UTF-8 for universal language support
    location = location.decode(stdin.encoding).encode('utf-8')
    locale = locale.decode(stdin.encoding).encode('utf-8')

    # Normalize special characters to URL accepted codes
    location = urllib2.quote( location )
    locale = urllib2.quote( locale )

    # Use string formatting and template
    url = API_URL % ( location, locale )

    # This behaves somewhat like File I/O
    handler = urllib2.urlopen( url )

    if handler.getcode() is not 200:
        return "ERROR"
        # TODO: use actual Google feedback to give problem_cause

    # Prepare data
    raw_data = handler.read()
    encoding = handler.headers['content-type'].split('charset=')[-1]

    # Just like File I/O, close it as soon as we don't need it
    handler.close()

    # For non utf-8 cases
    if encoding is not 'utf-8':
        u_data = unicode( raw_data, encoding ).encode('utf-8')
    else:
        u_data = raw_data

    # Create a DOM object (DOM stands for Document Object Model)
    dom = minidom.parseString( u_data )

    # strip down the une
    weather_dom = dom.getElementsByTagName('weather')[0]

    return weather_dom
