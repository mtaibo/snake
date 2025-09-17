import curses

class Snake():
    def __init__(self, stdscr):

        self.stdscr = stdscr

        # Relative dimensions
        self.grid_height = 0
        self.grid_width = 0

        # Non customizable options
        self.lenght = 2 # Head not included
        self.direction = ord('s') # Initial direction
        self.location = {
            'head' : (self.grid_height//2, self.grid_width//2),
            'body' : [(self.grid_height//2-1, self.grid_width//2), 
                      (self.grid_height//2-2, self.grid_width//2)]} 

        # Customizable options
        self.movement_keys = [ord('w'), ord('a'), ord('s'), ord('d')]
        self.snake_characters = {
            'head': {
                ord('w'): '▲', # Head up
                ord('a'): '◀', # Head left
                ord('s'): '▼', # Head down
                ord('d'): '▶', # Head right
            }, 'body': '█'}


    def display(self):

        # Display head


        for 

    def move(self, direction):
        pass

    def grow(self):
        pass