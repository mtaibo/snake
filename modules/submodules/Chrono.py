import time


class Chrono():

    def __init__(self, stdscr):
        self.stdscr = stdscr
        
        self.start_time = 0
        self.accumulated_time = 0

    def display(self):
        pass
    
    def start(self):
        self.start_time = time.monotonic()

    def pause(self):
        self.accumulated_time += time.monotonic() - self.start_time
