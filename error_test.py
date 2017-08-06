import urllib2

request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
	urllib2.urlopen(request)
except urllib.URLError, e:
	print e.reason
