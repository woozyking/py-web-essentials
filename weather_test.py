# weather_test

from pwe.weather import weather
import pprint

sep = "=" * 5

# Get weather
location = "McMaster University"
feedback = weather.get_weather(location)
forecast = feedback.forecast()

##print sep, "Everything (in dict type)", sep
##pprint.pprint( feedback.raw() )
##print

print sep, "Information Header (in dict type)", sep
pprint.pprint( feedback.information() )
print

print sep, "Current Conditions (in dict type)", sep
pprint.pprint( feedback.current() )
print

print sep, "Forecast (manipulated)", sep
for i in forecast:
    print i['day_of_week'] + ":"
    print "\t Condition: " + i['condition']
    print "\t High: " + i['high']
    print "\t Low: " + i['low']
    print "-" * 5
print
