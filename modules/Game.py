# Import game submodules
from modules.submodules.Chrono import Chrono
from modules.submodules.Grid import Grid
from modules.submodules.Snake import Snake
from modules.submodules.Food import Food

# Import module and template for Menus
from modules.Menu import Menu
from templates.menus import *

# Import standard library
import time



class Game():

    def __init__(self, stdscr, save):

        self.stdscr = stdscr
        self.save = save

        # Initialize submodules
        self.chrono = Chrono(stdscr)
        self.menu = Menu(stdscr)
        self.food = Food(stdscr)
        self.snake = Snake(stdscr)
        self.grid = Grid(stdscr)
    
    def set(self):
        
        # Set grid dimensions at Snake
        self.snake.grid_height = self.grid.height
        self.snake.grid_width = self.grid.width
        self.snake.height_corrector = self.grid.grid_top_left_corner_height
        self.snake.width_corrector = self.grid.grid_top_left_corner_width
        self.snake.location = {
            'head' : [self.snake.grid_height//2, self.snake.grid_width//2],
            'body' : [[self.snake.grid_height//2-1, self.snake.grid_width//2], 
                      [self.snake.grid_height//2-2, self.snake.grid_width//2]]} 

        # Set grid dimensions at Chrono
        self.chrono.grid_top_right_corner_height = self.grid.grid_top_left_corner_height + self.grid.height
        self.chrono.grid_top_right_corner_width = self.grid.grid_top_left_corner_width + self.grid.width

    def start(self):
        
        # Set game parameters to default
        self.set()

        # First time menu 
        if self.save.first_time: self.menu.deploy(first_time_menu)

        # Initialize game
        self.grid.countdown()
        self.chrono.start()
        self.key = self.snake.direction
        
        # Main game loop
        while self.snake.game_over == False:
            
            self.grid.display()
            self.food.display()
            self.snake.display()
            self.chrono.display()

            self.stdscr.refresh()

            self.key = self.stdscr.getch()
            self.stdscr.timeout(0)

            # Pause and Quit controls
            if self.key == ord('q'): return
            elif self.key == ord('p'):
                self.chrono.pause()
                self.menu.deploy(pause_menu)

                if self.menu.key_pressed == 1: 
                    self.chrono.start()
                    self.grid.countdown() 
                elif self.menu.key_pressed == 2: return

            # Snake movement control
            elif self.key in self.snake.movement_keys and self.key != self.snake.direction:
                self.snake.direction = self.key
                self.snake.direction_changed = True

            # Game time control
            self.snake.move()       
            time.sleep(0.3)