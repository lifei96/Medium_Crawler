# encoding: utf-8
import random
import time
from selenium import webdriver

class User(object):
	def __init__(self):
		super(User, self).__init__()
		self.data = {
			'ID' : -1,#帐号
			'Name' : -1,#姓名
			'Description' : "",#个人描述
			'Following' : 0,#关注数量
			'Followers' : 0,#被关注数量
			'Twitter_ID' : -1,#Twitter帐号
			'Facebook_ID' : -1,#Facebook帐号
		}
	
	def getstr(self):
		result = "{\n"\
		+ '    \"ID\": \"' + str(self.data['ID']) + "\",\n"\
		+ '    \"Name\": \"' + str(self.data['Name']) + "\",\n"\
		+ '    \"Description\": \"' + str(self.data['Description']) + "\",\n"\
		+ '    \"Following\": ' + str(self.data['Following']) + ",\n"\
		+ '    \"Followers\": ' + str(self.data['Followers']) + ",\n"\
		+ '    \"Twitter_ID\": \"' + str(self.data['Twitter_ID']) + "\",\n"\
		+ '    \"Facebook_ID\": \"' + str(self.data['Facebook_ID']) + "\",\n}"
		return result

def get_profile(ID, driver):
	url = "https://medium.com/@" + str(ID)
	driver.get(url)
	time.sleep(2)
	user = User()
	user.data['ID'] = ID
	user.data['Name'] = driver.find_element_by_class_name("hero-title").text
	if driver.find_element_by_class_name("hero-description ") != -1:
		user.data['Description'] = driver.find_element_by_class_name("hero-description ").text
	button_list = driver.find_elements_by_class_name("button")
	for button in button_list:
		if button.get_attribute("data-action-value") == "following":
			user.data['Following'] = int(filter(str.isdigit, str(button.get_attribute("title"))))
		if button.get_attribute("data-action-value") == "followers":
			user.data['Followers'] = int(filter(str.isdigit, str(button.get_attribute("title"))))
		if button.get_attribute("title") == "Twitter":
			user.data['Twitter_ID'] = str(button.get_attribute("href"))[20:]
		if button.get_attribute("title") == "Facebook":
			user.data['Facebook_ID'] = str(button.get_attribute("href"))[21:]
	return user
