import urllib2
import urllib

data ={}

data['name'] = 'WHY'
data['location'] = 'SDU'
data['language'] = 'Python'

url_values = urllib.urlencode(data)
print url_values

url = 'http://blog.csdn.net/pleasecallmewhy/article/details/8923067'
full_url = url + '?' + url_values

data = urllib2.urlopen(full_url)
print data.read()
