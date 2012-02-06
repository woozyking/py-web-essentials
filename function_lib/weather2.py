'''
Module: py-web-essentials.function_lib.weather (TODO: proper packages)
Author: oEL
Version: 1.0
Description:
A python wrapper of the unofficial Google Weather API:
http://www.google.com/ig/api?weather={location}&hl={locale}
Handles different languages properly
Known issues: none
TODO & FIXME: see in-line comments
'''

from sys import stdin
import urllib2 # for urlopen
import urllib # for urlencode

# use the C implementation of xml.etree.ElementTree
from xml.etree import cElementTree as ET

# bunch of configurables, reflects the current Google Weather API
# TODO: objectify the lib and make configurations easier
API_VER = '1'
API_URL = "http://www.google.com/ig/api?weather=%s&hl=%s"

REPLY_TAG = 'xml_api_reply' # to get version
WEATHER_TAG = 'weather' # actual root for weather info
MISC_INFO_TAG = 'forecast_information' # misc info
CURRENT_TAG = 'current_conditions'
FORECAST_TAG = 'forecast_conditions'
VERSION_ATT = 'version'

# temp utility functions, TODO: needs refactoring
def unicode_s( s ):
    '''
    unicode_s( s ) -> unicode str (<type 'unicode'>)

    Returns the unicode version of the input string.
    Codec used depends on OS setup: see sys.stdin.encoding for details
    '''
    return unicode( s, stdin.encoding ).encode('utf-8')

def norm_url( base_url, location ):
    location = urllib2.quote( unicode_s(location) )

    if locale is not '':
        locale = urllib2.quote( unicode_s(locale).encode('utf-8') )

    return base_url % ( location, locale )

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
        ** Province/state and country are optional,
        ** Though you might get an unwanted city

    locale - (case insensitive) [optional], output language, see:
        https://sites.google.com/site/tomihasa/google-language-codes
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

    # Get the current character set
    encoding = handler.headers['content-type'].split('charset=')[-1]

    # Prepare data
    raw_data = handler.read()

    # Just like File I/O, close it as soon as we don't need it
    handler.close()

    # Forcing data to be encoded with UTF-8
    if encoding is not 'utf-8':
        u_data = unicode( raw_data, encoding ).encode('utf-8')
    else:
        u_data = raw_data

    element = ET.XML( u_data )

    return element
