# geo_test.py

from pwe.maps import geocode
import pprint

sep = "=" * 5

# get geocode
location    = "McMaster University"
geo         = geocode.geo_lookup( location )

print sep, "Geocode of", location, "in JSON", sep

pprint.pprint( geo )

# reverse lookup
lat = "43.2683618"
lng = "-79.9135276"
rev = geocode.reverse_lookup( lat, lng )

print sep * 10
print sep, "Reverse lookup for",
print "Latitude:", lat, "& Longitude:", lng,
print "in JSON", sep

pprint.pprint( rev )
