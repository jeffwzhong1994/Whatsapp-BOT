#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import time
import pandas as pd
import socket

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)

time.sleep(25)

def readContacts(fileName):
    lst = []
    file = pd.read_excel(fileName, header = None)

    for name in file[0]:
    	lst.append(name)
    return lst

targets = readContacts("./name.xlsx")


# string = sys.argv[1]
string = '测试....'

for target in targets:
	try:
		x_arg = '//span[contains(@title,' + '"' + target + '"' + ')]'
		group_title = wait.until(EC.presence_of_element_located(( 
	    By.XPATH, x_arg)))

	except:
		search = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/input')[0]
		search.clear()
		search.send_keys(target)
		time.sleep(3)

	    # click the search button
		x_arg = '//span[@class="_3NWy8"]/span[contains(@title,' + '"' + target + '"' + ')]'
		group_title = wait.until(EC.presence_of_element_located(( 
	    By.XPATH, x_arg)))

	group_title.click() 
	time.sleep(5)
	message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

	for i in range(3):
		message.send_keys(string)
		sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
		sendbutton.click()
		time.sleep(1)

