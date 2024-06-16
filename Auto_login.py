from selenium import webdriver
import random
import os
from dotenv import load_dotenv
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

#random user agent to send to server
user_agents= ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
              'Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36'
              ]


#randomiozing agent sent
user_agent_string =random.choice(user_agents)

options.add_argument(f"user-agent={user_agent_string}")

driver=webdriver.Chrome(options=options)
url='https://www.geeksforgeeks.org/'

driver.get(url)

#get full windows

driver.maximize_window()
time.sleep(3)

#finding sign in button and click

sign_in=driver.find_element(By.CLASS_NAME,'header-main__signup.login-modal-btn').click()
time.sleep(3)

#getting the pop up loging box
login=driver.find_element(By.ID,'Login')
time.sleep(5)

load_dotenv()
username =os.getenv("LOGER")
password=os.getenv("PASSWORD")
#extracting username and password
username=login.find_element(By.ID,'luser').send_keys(username)
password=login.find_element(By.ID,'password').send_keys(password)
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

# finding profile button to user's dashboard and clicking
time.sleep(6)
driver.find_element(By.CLASS_NAME,'profileCard-profile-picture').click()
time.sleep(5)

#finding profile page
driver.find_element(By.PARTIAL_LINK_TEXT,'My Profile').click()

time.sleep(8)

driver.quit()
#profile.find_element(By.PARTIAL_LINK_TEXT,'https://www.geeksforgeeks.org/user/').click()


