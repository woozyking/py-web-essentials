# places_test

from pwe.maps import places
import pprint

### Find place
# Prepare request
location = "43.2683618,-79.9135276" # must be in lat,lng format
name = "mcmaster" # name searching for
radius = "500" # radius in meters
sensor = False # False by default
places.API_KEY = "" # get your own from https://code.google.com/apis/console

place = places.find_place( name=name, location=location, radius=radius, sensor=sensor )

pprint.pprint(place)
