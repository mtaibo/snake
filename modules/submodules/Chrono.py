# Import standard library
import time


class Chrono():

    def __init__(self, stdscr):
        self.stdscr = stdscr

        # Grid chrono position
        self.grid_top_right_corner_height = 0
        self.grid_top_right_corner_width = 0
        
        # Chrono variables
        self.start_time = 0
        self.accumulated_time = 0

    def display(self):
        
        minutes, seconds = divmod(int(self.accumulated_time + time.monotonic() - self.start_time), 60)
        formatted_time = f'Time: {minutes:02d}:{seconds:02d}s'
        
        self.stdscr.addstr(self.grid_top_right_corner_height-1, 
                           self.grid_top_right_corner_width-len(formatted_time), 
                           formatted_time)
    
    def start(self):
        self.start_time = time.monotonic()

    def pause(self):
        self.accumulated_time += time.monotonic() - self.start_time
