import datetime
from dotenv import load_dotenv
import os

def showtime():

    return str(datetime.datetime.now().strftime("%H:%M, %d_%m_%y"))



me=showtime()
print(me)

load_dotenv()
username:str =os.getenv("LOGER")
password:str =os.getenv("PASSWORD")

print(username)
print(password)