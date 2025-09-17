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

        self.set() # Set game parameters from save
    
    def set(self):
        
        # Set grid dimensions at Snake
        self.snake.grid_height = self.grid.height
        self.snake.grid_width = self.grid.width

    def start(self):

        # First time menu 
        if self.save.first_time: self.menu.deploy(first_time_menu)

        # Initialize game
        self.grid.countdown()
        self.chrono.start()
        
        # Main game loop
        while True:
            
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

                if self.menu.key_pressed == 1: self.chrono.start() 
                elif self.menu.key_pressed == 2: return

            # Movement controls
            '''
            elif self.key in self.snake.movement_keys:
                self.snake.move(self.key)
                self.food.check(self.snake.location)           
            '''

            # Game time control
            time.sleep(0.1)