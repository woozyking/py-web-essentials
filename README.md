# Py-Web-Essentials (PWE)

## Goal:

Provide convenient means to access the WWW (that your grandparents could start using Python).

## Features:

(available once stable)

## Changelog:

* v0.1.5:
  * Weather (pwe.weather)
    * weather.py and weather2.py unified into one (weather.py), pretty much re-written
	* Fully convert ElementTree to JSON (dict type), thanks to s-ltf <https://github.com/s-ltf>
	* Objectified for further extensibility
  * util.py cleaned up and all relevant code verified
  * Demo added for all 4 libraries available now (find under the root of the project repo)

* v0.1 (fun-functions):
  * Weather (pwe.weather)
    * weather.py (minidom XML implementation), and weather2.py (ElementTree)
  * Google Maps (pwe.maps)
    * Geocode lookup and reverse lookup
	* Places search
  * URL (pwe.url)
    * goo.gl URL shortening and expanding

## Known Issues:

Still in a highly WIP status, currently developed and tested under Python 2.7.x environment only (mostly Windows).

## TODO:

* Google Tasks API
* Generic OAuth Wrapper
* Unit testing, exception handling, data encapsulation (where needed) and a lot of those tedious "best practices"

## License

Released under the FreeBSD license:

Copyright (c) 2012 The Py-Web-Essentials (PWE) Team

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE FREEBSD PROJECT ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE FREEBSD PROJECT OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Team

* oEL <https://github.com/ruli>
* s-ltf <https://github.com/s-ltf>
* YOU, yeah YOU! Join us by forking this repo, feed this baby by making pull requests!