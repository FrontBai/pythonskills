import urllib2
req = urllib2.Request('http://www.python.org/')
response = urllib2.urlopen(req)
url = response.geturl()
info = response.info()
code = response.getcode()
print url, '\n', info, '\n', code
