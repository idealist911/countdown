# reference: https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/

import time

def Countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        timer = '{:02}:{:02}:{:02}'.format(hrs, mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Time's up!")

t = int(input('Enter time in seconds: '))
Countdown(t)
