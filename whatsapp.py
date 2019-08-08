#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time
import pandas as pd
import socket

# Function for reading all their contacts:
def readContacts(fileName):
    lst = []
    file = pd.read_excel(fileName, header = None)

    for name in file[0]:
    	lst.append(name)
    return lst
 
#This function would grab all the contact member's name and phone number from target lists:
def get_names_in_group(targets):

	contact_list = []

	for target in targets:
		search = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/input')[0]
		search.clear()
		search.send_keys(target)
		time.sleep(3)

	    # click the search button
		# x_arg = '//span[@class="_3NWy8"]/span[contains(@title,' + '"' + target + '"' + ')]'
		x_arg = '//div[@class="_3H4MS"]/span[contains(@title,' + '"' + target + '"' + ')]'
		group_title = wait.until(EC.presence_of_element_located(( 
	    By.XPATH, x_arg)))
		group_title.click()
		time.sleep(4)

		for contactlists in driver.find_elements_by_xpath('//div[@class="_3Q3ui i1XSV"]/span[@title]'):
			title = contactlists.get_attribute('title')
			contact_list.append(title)
			print(title)
		time.sleep(3)
		
	print(contact_list)
	contact_list = pd.DataFrame(contact_list)
	contact_list.to_excel('./contactlists.xlsx', index = False, header = False)

#Group send message:
def send_messages(targets):

	#Message to sent:
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

# Scroll down to get all contact's lists:
def get_contacts():

	lst1 = []
	#Determine For Loop's running time on how long your contact lists are:
	REPEATED_TIMES = 150
	for i in range(REPEATED_TIMES):
		for person in driver.find_elements_by_xpath('//div[@class="_3H4MS"]/span[@title]'):
			try:
				title = person.get_attribute('title')
				lst1.append(title)
			except:
				continue	
		time.sleep(2)

	lst1 = pd.DataFrame(lst1)
	lst1.to_excel('./contact_name.xlsx', index = False)

def main():
	driver = webdriver.Firefox(executable_path = './geckodriver')
	# driver = webdriver.Chrome('./chromedriver')
	driver.get('https://web.whatsapp.com/')
	wait = WebDriverWait(driver, 1000)
	time.sleep(15)

	#Maximize windows:
	driver.maximize_window()

	#Read contacts from Excel:
	targets = readContacts("./names.xlsx")

	#Run functions:
	get_names_in_group(targets)
	send_messages(targets)
	get_contacts()


if __name__ == '__main__':
    main()
