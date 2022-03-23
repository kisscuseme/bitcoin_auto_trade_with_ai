isRunning = True
baseInterval = 'minute60'

def get_base_interval():
    return baseInterval

def get_running():
    return isRunning

def set_running(flag):
    global isRunning
    isRunning = flag