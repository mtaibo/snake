import curses

class Snake():
    def __init__(self, stdscr):
        self.stdscr = stdscr

        '''Relativizar las medidas del grid'''
        # Grid dimensions
        self.grid_height = 24
        self.grid_width = 48

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

    
    def display(self):  
        # Display the snake's body
        for idx, (y, x) in enumerate(self.location):
            if idx == 0:
                self.stdscr.addstr(y, x, self.head_character, curses.color_pair(self.color_pair))
            else:
                self.stdscr.addstr(y, x, self.body_character, curses.color_pair(self.color_pair))
    
    def move(self, key):
        if key in self.movement_keys:
            self.direction = key
        
        head_y, head_x = self.location[0]

        if self.direction == ord('w'):
            new_head = (head_y - 1, head_x)
        elif self.direction == ord('s'):
            new_head = (head_y + 1, head_x)
        elif self.direction == ord('a'):
            new_head = (head_y, head_x - 1)
        elif self.direction == ord('d'):
            new_head = (head_y, head_x + 1)
        else:
            new_head = (head_y, head_x) 