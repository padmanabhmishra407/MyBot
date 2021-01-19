import urlTime
import time
import webbrowser
import schedule
import datetime
import os
import multiprocessing
# from datetime import datetime


# now = datetime.now()  # current date and time
#
# Day = now.strftime("%a")
#
# Time = now.strftime("%H:%M")
# def Tim():
#     while 1:
#
#       now = datetime.datetime.now()
#       T = now.strftime("%H:%M:%S")
#       time.sleep(1)
#       print(T,end="\r")

def Time():
    from datetime import datetime
    now = datetime.now()
    tim=now.strftime("%H:%M:%S")
    return tim

# def Open():
#         webbrowser.open("google.com")
def Da():
    while 1:
        now = datetime.datetime.now()
        Day = now.strftime("%a")
        time.sleep(1)
        return Day
        # time.sleep(1)

def C_1():
    webbrowser.open(urlTime.ES)
def C_2():
    webbrowser.open(urlTime.OT)
def C_3():
    webbrowser.open(urlTime.PC)
def C_4():
    webbrowser.open(urlTime.SPM)
def C_5():
    webbrowser.open(urlTime.DS)
def C_6():
    webbrowser.open(urlTime.DS_Lab)
def C_7():
    webbrowser.open(urlTime.EM_Lab)
def C_8():
    webbrowser.open(urlTime.VSR_Lab)

# def Testday():
#     print(Day,Time)
#
#     schedule.every().monday.at("18:13").do(C_1)
#     schedule.every().monday.at("18:14").do(C_2)
#     schedule.every().monday.at("17:54").do(C_3)
#     schedule.every().monday.at("17:55").do(C_8)
#     schedule.every().monday.at("17:56").do(C_8)
#     schedule.every().monday.at("17:57").do(C_4)
#
#     while Day=="Mon":
#         schedule.run_pending()
#         time.sleep(1)


def Monday():
    print(Da(),Time())
    schedule.every().monday.at(urlTime.A).do(C_1)
    schedule.every().monday.at(urlTime.B).do(C_2)
    schedule.every().monday.at(urlTime.D).do(C_3)
    schedule.every().monday.at(urlTime.E).do(C_8)
    schedule.every().monday.at(urlTime.F).do(C_8)
    schedule.every().monday.at(urlTime.G).do(C_4)

    while Da()=="Mon":
        schedule.run_pending()
        time.sleep(1)

def Tuesday():
    print(Da(),Time())
    schedule.every().tuesday.at(urlTime.A).do(C_4)
    schedule.every().tuesday.at(urlTime.B).do(C_1)
    schedule.every().tuesday.at(urlTime.C).do(C_3)
    schedule.every().tuesday.at(urlTime.D).do(C_2)
    schedule.every().tuesday.at(urlTime.E).do(C_8)
    schedule.every().tuesday.at(urlTime.F).do(C_8)
    schedule.every().tuesday.at(urlTime.G).do(C_8) #confirm schedule timing Em or Vsr Lab

    while Da()=="Tue":
        schedule.run_pending()
        time.sleep(1)

def Wednesday():
    print(Da(),Time())
    schedule.every().wednesday.at(urlTime.A).do(C_3)
    schedule.every().wednesday.at(urlTime.B).do(C_5)
    schedule.every().wednesday.at(urlTime.C).do(C_1)
    schedule.every().wednesday.at(urlTime.D).do(C_2)
    schedule.every().wednesday.at(urlTime.E).do(C_8)
    schedule.every().wednesday.at(urlTime.F).do(C_8)

    while Da()=="Wed":
        schedule.run_pending()
        time.sleep(1)

def Thursday():
    print(Da(),Time())
    schedule.every().thursday.at(urlTime.A).do(C_3)
    schedule.every().thursday.at(urlTime.B).do(C_5)
    schedule.every().thursday.at(urlTime.C).do(C_6)
    schedule.every().thursday.at(urlTime.D).do(C_6)
    schedule.every().thursday.at(urlTime.E).do(C_7)
    schedule.every().thursday.at(urlTime.F).do(C_7)

    while Da()=="Thu":
        schedule.run_pending()
        time.sleep(1)

def Friday():
    print(Da(),Time())
    schedule.every().friday.at(urlTime.A).do(C_4)
    schedule.every().friday.at(urlTime.D).do(C_3)
    schedule.every().friday.at(urlTime.E).do(C_3)

    while Da()=="Thu":
        schedule.run_prnding()
        time.sleep(1)

def ST():
            # return Day
            # time.sleep(1)


    # schedule.every().monday.do(Testday)
    # schedule.every().monday.do(Monday)
    # schedule.every().monday.do(Tuesday)
    # schedule.every().monday.do(Wednesday)
    # schedule.every().monday.do(Thursday)
    # schedule.every().monday.do(Friday)
    #
    # while 1:
    #     schedule.run_pending()
    #     time.sleep(1)
    while 1:
        if Da()=="Mon":
            # Testday()
            Monday()
            return ST()
        if Da()=="Tue":
            Tuesday()
            return ST()
        if Da=="Wed":
            Wednesday()
            return ST()
        if Da()=="Thu":
            Thursday()
            return ST()
        if Da()=="Fri":
            Friday()
            return ST()


ST()
