# encoding: utf-8
import time
import codecs
import os
import random
import medium_u_profile_crawler
import medium_u_following_crawler
import medium_u_followers_crawler
from selenium import webdriver

def get(ID):
	driver = webdriver.Firefox()
	print (ID)
	try:
		time.sleep(random.randint(2, 3))
		profile_str = medium_u_profile_crawler.get_profile(ID, driver).getstr()
		out = codecs.open("./Data/%s_profile.txt"%str(ID), 'w', 'utf-8')
		out.write(profile_str + "\n")
		out.close()
		print("-----profile obtained")
		time.sleep(random.randint(2, 3))
		following_str = medium_u_following_crawler.get_following(ID, driver).getstr()
		out = codecs.open("./Data/%s_following.txt"%str(ID), 'w', 'utf-8')
		out.write(following_str + "\n")
		out.close()
		print("-----following obtained")
		time.sleep(random.randint(2, 3))
		followers_str = medium_u_followers_crawler.get_followers(ID, driver).getstr()
		out = codecs.open("./Data/%s_followers.txt"%str(ID), 'w', 'utf-8')
		out.write(followers_str + "\n")
		out.close()
		print("-----followers obtained")
	except:
		driver.close()
		raise
	driver.close()
	
