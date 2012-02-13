import weather
import pprint

# Getting Weather information for McMaster University

location = "McMaster University"

data = weather.get_weather(location)

print "ugly looking block of code\n"
print data

print "-" * 20

print

print "better looking code using pprint module\n"
pprint.pprint( data )

