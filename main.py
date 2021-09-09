import datetime


def getTime():
    current_time = datetime.datetime.now()
    return current_time

def getTimeFormatted():
    return getTime().strftime("%I:%M %p")


def timeUntil():
    return (new_time - getTime())


def timeUntilFormatted():
    return timeUntil() - datetime.timedelta(microseconds=timeUntil().microseconds)


def setTimer(day=0, hr=0, min=0):
    time_change = datetime.timedelta(days=day, hours=hr, minutes=min)
    expectedTime(time_change)
    print("Set Timer ", expectedTime(time_change))


def expectedTime(tChange):
    global new_time
    new_time = getTime() + tChange
    return new_time


def getExpectedTimeFormatted():
    return new_time.strftime("%I:%M:%S %p\n \t   %D")


def timeCompare():
    if new_time <= getTime():
        return True
    else:
        return False

