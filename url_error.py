import urllib2
req = urllib2.Request('https://www.google.co.jp/?gfe_rd=cr&ei=O0dvWc7jLerC8gevnLrYDQ&gws_rd=ssljdkjlajfjd')
try:
	response = urllib2.urlopen(req)
#	print response.read()
	url = response.geturl()
	info = response.info()
	code = response.getcode()
	print url, '\n', info, '\n', code
except urllib2.URLError,e:
	print e.reason
	print e.reason[0]
	print e.reason[1]

