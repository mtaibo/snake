import threading
import time

'''
class Chronometer(threading.Thread()):
    def __init__(self, stdscr):
        super().__init__()
        self.stdscr = stdscr

        self.miliseconds = 00
        self.seconds = 00
        self.minutes = 00

        self.wait = threading.Event()
        self.running = False
        self.stop = False
    
    def run(self):
        if not self.running:
            self.running = True
            while not self.stop:
                if self.running:
                    if self.miliseconds == 1000:
                        self.miliseconds = 0
                        self.seconds += 1
                    
                    if self.seconds == 60:
                        self.seconds = 0
                        self.minutes += 1
                    
                    if self.minutes == 60:
                        self.miliseconds = 0
                        self.seconds = 0
                        self.minutes = 0

                    self.current_time = f'{self.minutes:02}:{self.seconds:02}:{self.miliseconds//10:02}'
                    
                    self.miliseconds += 10
                    time.sleep(0.01)

                elif self.running is False:
                    self.wait.clear()
                    self.wait.wait()

        if not self.running:
            self.running = True
            while self.running:
                if self.miliseconds == 1000:
                    self.miliseconds = 0
                    self.seconds += 1
                
                if self.seconds == 60:
                    self.seconds = 0
                    self.minutes += 1

                self.current_time = f'{self.minutes:02}:{self.seconds:02}:{self.miliseconds//10:02}'

                self.miliseconds += 10
                time.sleep(0.01)
    
    def pause(self):
        if self.running:
            self.running = False
            if self.chronometer_thread is not None:
                self.chronometer_thread.join()
    
    def stop(self):
        self.running = False
        if self.chronometer_thread is not None:
            self.chronometer_thread.join()

'''