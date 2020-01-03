#!/usr/bin/env python3
import sys
import time
import pickle
import argparse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from sty import fg, bg, ef, rs

options = Options()

options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
browser = webdriver.Chrome(options=options)

dorks 	= open('dorks.txt', 'r')
target 	= ''
query 	= 'https://www.google.com/search?ei=Rar6XdWJDe2g5OUPvs2MmAM&q='



def check_vulnerability(browser, target, dork):
	url = '%s%s site:%s'%(query, dork, target)
	browser.get(url)
	try:
		#Search for reCaptcha
		browser.find_element_by_id('captcha-form')
		input('\nGoogle is trying to block you... solve captcha and hit enter when ready.\n')
	except:
			dork = dork.strip()
			try:
				browser.find_element_by_id('resultStats')
				print(bg(1)+fg(15)+"[ *** VULNERABILITY DETECTED! *** ] - %s site:%s"%(dork, target)+fg.rs+bg.rs)
				output.append('%s site:%s'%(dork, target))
			except:
				print('Dork failed - %s site:%s'%(dork, target))


for dork in dorks:
	check_vulnerability(browser, target, dork)

browser.close()
