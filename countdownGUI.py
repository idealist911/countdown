# ==================================== #
# A countdown timer
# What it does:
# 1. Given the countdown duration,
# 2. The timer counts down to zero
# ==================================== #

import sys
import time
import tkinter as tk

class Countdown():
    def __init__(self, t):
        self.duration = t # save the original t so to allow reset
        self.t = t # time in seconds. Will keep decreasing over time.
        self.run = 1 # to stop timer

        self.FONT = 'Arial'
        self.FONTSIZE = 120

        self.window = tk.Tk()
        self.window.title('Countdown Timer')
        
        self.label = tk.Label(
                text=self.gettime(t), # express time in hours:mins:secs 
                font=(self.FONT, self.FONTSIZE))
        self.label.grid(row=0, columnspan=3)
        
        self.btnStart = tk.Button(
                text='Start',
                font=(self.FONT, int(self.FONTSIZE/2)),
                command=self.start)
        self.btnStart.grid(
                row=1, column=0, 
                #sticky='W', 
                padx=5, pady=5)

        self.btnStop = tk.Button(
                text='Stop',
                font=(self.FONT, int(self.FONTSIZE/2)),
                command=self.stop)
        self.btnStop.grid(
                row=1, column=1, 
                #sticky='', 
                padx=5, pady=5)

        self.btnReset = tk.Button(
                text='Reset',
                font=(self.FONT, int(self.FONTSIZE/2)),
                command=self.reset)
        self.btnReset.grid(
                row=1, column=2, 
                sticky='E', 
                padx=5, pady=5)

        #self.window.after(0, self.update) # updates the label immediately
        self.window.mainloop()

    def gettime(self,t):
        # returns time in seconds as a string in hours:mins:secs
        # reference: https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        TIME = '{:02}:{:02}:{:02}'.format(hrs, mins, secs)
        return TIME

    def reset(self):
        self.run = 1
        self.t = self.duration
        self.label.configure(text=self.gettime(self.t), font=(self.FONT, int(self.FONTSIZE)))

    def start(self):
        self.run = 1
        self.window.after(0, self.update)

    def stop(self):
        self.run = 0

    def update(self):
        # https://stackoverflow.com/questions/66361332/creating-a-timer-with-tkinter
        t = self.t
        if t > 0:
            self.label.configure(text=self.gettime(t), font=(self.FONT, self.FONTSIZE))
            t -= 1
            self.t = t
            if self.run:
                self.window.after(1000, self.update) # update every 1 second (i.e. 1000 ms)
        else:
            self.label.configure(text="Time's up!", font=(self.FONT, self.FONTSIZE))


# MAIN #
if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <time in seconds>')
    sys.exit(1)
main = Countdown(int(sys.argv[1]))
