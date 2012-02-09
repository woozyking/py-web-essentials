from pwe import util

API_URL = "http://maps.googleapis.com/maps/api/geocode/"
OUTPUT_FORMAT = "json" # can be xml

def geo_lookup( addr, lang='en' ):
    '''
geo_lookup( address, language ) -> JSON feedback <type 'dict'>

Parameters:
addr: address in string
lang: (Optional) desired language code in string
see http://goo.gl/Xj4Nx for details
'''
    url = util.norm_url( API_URL + OUTPUT_FORMAT, [], address=addr, language=lang, sensor=False )
    handler = util.open_url(url)

    return util.get_json(handler)

def reverse_lookup( lat, lng, lang='en' ):
    '''
reverse_lookup( lat, lng, lang ) -> JSON feedback <type 'dict'>

Parameters:
lat: latitude in float or str
lng: longitude in float or str
lang: (Optional) desired language code in string
see http://goo.gl/Xj4Nx for details
'''
    ll = str(lat) + ',' + str(lng)
    url = util.norm_url( API_URL + OUTPUT_FORMAT, latlng=ll, sensor=False )
    handler = util.open_url(url)

    return util.get_json(handler)
