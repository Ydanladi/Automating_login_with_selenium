import datetime

def showtime():
    return str(datetime.datetime.now().strftime("%H:%M, %d_%m_%y"))

me=showtime()
print(me)