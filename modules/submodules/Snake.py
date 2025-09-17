import curses

class Snake():
    def __init__(self, stdscr):

        self.stdscr = stdscr

        '''Relativizar las medidas del grid'''
        # Grid dimensions
        self.grid_height = 0
        self.grid_width = 0

        # Non customizable options
        self.lenght = 2 # Head not included
        self.direction = ord('d')
        self.location = {
            'head' : (12, 24),
            'body' : [
                (12, 25), (12, 26),
            ]
        } 

        # Customizable options
        self.movement_keys = [ord('w'), ord('a'), ord('s'), ord('d')]
        self.snake_characters = {
            'body': '█',
            'head-up': '▲',
            'head-down': '▼',
            'head-left': '◀',
            'head-right': '▶',
        }


    def display(self):
        pass

    def move(self, direction):
        pass

    def grow(self):
        pass