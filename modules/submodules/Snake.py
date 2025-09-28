import curses

class Snake():
    def __init__(self, stdscr):

        self.stdscr = stdscr
        self.game_over = False

        # Relative dimensions
        self.grid_height = 0
        self.grid_width = 0

        # Position corrector
        self.height_corrector = 0
        self.width_corrector = 0

        # Non customizable options
        self.lenght = 2 # Head not included
        self.direction = ord('s') # Current direction
        self.location = {
            'head' : [self.grid_height//2, self.grid_width//2],
            'body' : [[self.grid_height//2-1, self.grid_width//2, 'vertical'], 
                      [self.grid_height//2-2, self.grid_width//2, 'vertical']]} 

        # Customizable options
        self.movement_keys = [ord('w'), ord('a'), ord('s'), ord('d')]
        self.snake_characters = {
            'head': {
                ord('w'): '▲', # Head up
                ord('a'): '◀', # Head left
                ord('s'): '▼', # Head down
                ord('d'): '▶', # Head right
            }, 'body': '■'} #'█'}

    def display(self):

        # Display head
        self.stdscr.addstr(self.location['head'][0]+self.height_corrector, 
                           self.location['head'][1]+self.width_corrector, 
                           self.snake_characters['head'][self.direction]) 

        # Display body
        for index, segment in self.location['body']:
            self.stdscr.addstr(segment[0]+self.height_corrector, 
                               segment[1]+self.width_corrector, 
                               self.snake_characters['body'])

    def move(self):

        # Update body location
        self.location['body'].insert(0, self.location['head'])
        if len(self.location['body']) > self.lenght: 
            last_location = self.location['body'].pop()
            self.stdscr.addstr(last_location[0]+self.height_corrector, 
                               last_location[1]+self.width_corrector, ' ')

        # Update body orientation
        if self.direction_changed:
           pass 

        '''
        The direction_changed flag is just for the first element of the body
        '''

        # Create new head location
        if self.direction == ord('w'): # Up
            new_location = [self.location['head'][0]-1, self.location['head'][1]]
        elif self.direction == ord('a'): # Left
            new_location = [self.location['head'][0], self.location['head'][1]-1]
        elif self.direction == ord('s'): # Down
            new_location = [self.location['head'][0]+1, self.location['head'][1]]
        elif self.direction == ord('d'): # Right
            new_location = [self.location['head'][0], self.location['head'][1]+1]
        
        # Check if new location is empty
        if chr(self.stdscr.inch(new_location[0], new_location[1]) & curses.A_CHARTEXT) == ' ':
            self.location['head'] = new_location # Update head location
        else: self.game_over = True # If not empty, game over 

    def grow(self):
        pass