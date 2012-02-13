
import weather
import pprint

# Getting Weather information for McMaster University

location = "McMaster University"

data = weather.get_weather(location)


print "ugly looking block of code\n",data

print

print "better looking code\n"
pprint.pprint( data )

