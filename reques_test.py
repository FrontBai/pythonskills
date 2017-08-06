import urllib2
import urllib
url = 'http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html'
values = {'name' : 'Michael Foord',
		  'location':'Northampton',
		  'language':'Python'}
data = urllib.urlencode(values)
print data		
req = urllib2.Request(url, data)
print req
response = urllib2.urlopen(req)
print response
the_page = response.read()
print the_page
