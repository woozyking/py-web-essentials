# url_test

from pwe.url import url_shortener
import pprint

sep = "=" * 5

# Shorten URL
long_url = "http://docs.python.org/tutorial/index.html"
feedback = url_shortener.shorten( long_url )

# pprint.pprint( feedback ) # prints the whole JSON feedback
print long_url, "shortened to:", feedback['id']

print sep * 10

# Expand URL
short_url = "http://goo.gl/c5GO"
feedback = url_shortener.expand( short_url )

# pprint.pprint( feedback ) # prints the whole JSON feedback
print short_url, "expanded to:", feedback['longUrl']
