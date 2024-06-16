from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import os
from dotenv import load_dotenv






#create a ChromeOptions instance
options = webdriver.ChromeOptions()

#random user agent to send to server
user_agents= ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
              'Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36'
              ]

# getting user details
# username=input('enter your username: ')
# password=input('enter your password: ')

# user={
#     'username':username,
#     'password':password
# }


#randomiozing agent sent
user_agent_string =random.choice(user_agents)

# run code in headless mode and useragent through option
options.add_argument(f"user-agent={user_agent_string}")
options.add_argument("--headless")
driver=webdriver.Chrome(options=options)

#url
url='https://auth.geeksforgeeks.org/'

driver.get(url)

#get full windows

driver.maximize_window()
time.sleep(3)

#getting the pop up loging box
login=driver.find_element(By.ID,'Login')
time.sleep(5)

load_dotenv('.env')
#extracting username and password
username=login.find_element(By.ID,'luser').send_keys(os.getenv("username"))
password=login.find_element(By.ID,'password').send_keys(os.getenv("password"))
time.sleep(2)
#logging in
log=login.find_element(By.CLASS_NAME,'btn.btn-green.signin-button').click()
time.sleep(6)
# skipping pop-up
skip=driver.find_element(By.ID,'lower_section_text')
if skip:
    skip.click()  
    time.sleep(5)
else:
    pass

# lambda function to use JS and the the full with and height of the site
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) 

time.sleep(3)
#creating function to save screenshot with date and time

driver.find_element(By.TAG_NAME,'body').screenshot('data/image.png')
time.sleep(3)
