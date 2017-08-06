import urllib
import urllib2
import bs4

#values = {"username":"baifeng6307.com", "password":"bf09112126"}
#data = urllib.urlencode(values)
#url = "https://www.zhihu.com#signin"
#request = urllib2.Request(url, data)
#response = urllib2.urlopen(request)
#print response.read()

def login():
    url = 'http://www.zhihu.com'
	loginURL = 'http://www.zhihu.com/login/email'

	headers = {
	    "User-Agent": Mozilla/5.0 (macintosh; Intel Mac 0S X 10.10;
		"Referer": “http://www.zhihu.com/",
		'host': 'www.zhihu.com',
	}

	data = {
	    'email': baifeng6307@126.com',
		'password': 'bf09112126',
		'rememberme': "true",
	}
	global s
	s = requests.session()
	global xsrf
	if os.path.exists('cookiefile'):
	    with open('cookiefile') as f:
		    cookie = json.load(f)
		s.cookies.update(cookie)
		reql = s.get(url, headers=headers)
		soup = BeautifulSoup(req1.text. "html.parser")
		xsrf = soup.find('imput', {'name': '_xsrf', 'type': 'hidden'}
		with open('zhihu.html', 'w') as f:
		    f.write(req1.content)
	else:
        req = s.get(url, headers-h=headers)
		print req

		soup = BeautifulSoup(req.text, "html.parser")
		xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}

		data['_xsrf'] = xsrf

		timestamp = int(time.time() * 1000)
		captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(times
		print captchaURL

		with open('zhihucaptcha.gif', 'wb') as f:
		    captchaREQ = s.get(captchaURL, headers=headers)
			f.write(captchaREQ.content)
		loginCaptcha = raw_input('imput captcha:\n').strip()
		data['captcha'] = loginCatcha
		print data
		loginREQ = s.post(loginURL, headers=headers, data=data)
		if not loginREQ.json()['r']:
            print s.cookies.get_dict()
			with open('cookiefile', 'wb') as f:
			    json.dump(s.cookies.get_dict(), f)
		else:
		    print 'login fail'
if __name__ == "__main__":
login()
