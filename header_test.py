import urllib
import urllib2

url = 'http://blog.csdn.net/pleasecallmewhy/article/details/8923067'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
values = {'name': 'WHY',
		  'location' : 'SDU',
		  'language' : 'Python'}

headers = {'User-Agent' : user_agent}
print headers
data = urllib.urlencode(values)
print data
req = urllib2.Request(url, data, headers)
print req
req.add_header('Referer', 'http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html')
response = urllib2.urlopen(req)
print response
the_page = response.read()
print the_page
