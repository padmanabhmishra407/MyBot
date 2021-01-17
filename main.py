import urlTime
import func
import time
import schedule
from datetime import datetime
import os, sys
from guiLoop import guiLoop


# schedule.every(5).seconds.do(func.Run)


# schedule.every().day.at("22:04").do(func.Thursday)


now = datetime.now()  # current date and time

Day = now.strftime("%a")

@guiLoop
def File_1():

  

    Time = now.strftime("%H:%M:%S")
    print(Time)

    schedule.every().monday.at("09:20").do(func.Monday)
    schedule.every().tuesday.at("09:20").do(func.Tuesday)
    schedule.every().wednesday.at("09:20").do(func.Wednesday)
    schedule.every().thursday.at("09:20").do(func.Thursday)
    schedule.every().friday.at("09:20").do(func.Friday)

# def DaYs():
#     if Day == "Mon":
#         print("M")
#         schedule.every().day.at("09:20").do(func.Monday)
#     if Day == "Tue":
#         print("T")
#         schedule.every().day.at("09:20").do(func.Tuesday)
#     if Day == "Wed":
#         print("W")

#         schedule.every().day.at("09:20").do(func.Wednesday)
#     if Day == "Thu":
#         print("TH")
#         schedule.every().day.at("09:20").do(func.Thursday)
#     if Day == "Fri":
#         print("F")
#         schedule.every().day.at("09:20").do(func.Friday)
#     if Day == "Sat":
#         print("ELSE")
#         time.sleep(86400)
#     if Day == "Sun":
#         print("el2")
#         time.sleep(86400)

# schedule.every().day.at("9:20").do(DaYs)

# schedule.every(86400).seconds.days.at("09:20").do(DaYs) # refresh every 24Hrs (no much useful)

    while 1:
        schedule.run_pending()
        time.sleep(1)


# def ExitMain():
#     sys.exit(r"D:\Projects\MyBot\main.py")