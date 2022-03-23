import datetime

checkSelect = True
checkSell = True
nextTime = None

def target_time(interval):
    global checkSelect, checkSell, nextTime
    now = datetime.datetime.now()
    nextTime = now.hour
    theTime = datetime.datetime(now.year, now.month, now.day, nextTime) + datetime.timedelta(minutes = interval)

    if theTime < now < theTime + datetime.timedelta(seconds=10):
        return True
    else:
        return False