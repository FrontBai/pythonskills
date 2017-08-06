import os
from selenium import webdriver

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrom.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.baidu.com/')
#browser.quit()
