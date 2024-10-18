import time
import random
import math

def getRandomDate(startdate, enddate):
    print("Random date is ")
    dateFormat= '%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate,dateFormat))
    endtime=time.mktime(time.strptime(endtime, dateFormat))
    randomTime=random.randint(int(starttime, int(endtime)))
    randomdate=time.strftime(dateFormat, time.localtime(randomTime))
    return randomdate
print("Random date", getRandomDate("01/01/2024, 312/31/2024"))