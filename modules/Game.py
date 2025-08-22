#from modules.submodules.Chronometer import Chronometer
from modules.submodules.Grid import Grid
from modules.submodules.Snake import Snake
from modules.submodules.Food import Food

from modules.Menu import Menu
from templates.menus import *


class Game():
    def __init__(self, stdscr, save):

        self.stdscr = stdscr
        self.save = save

        # Inicializar todas las partes del juego

        self.menu = Menu(stdscr)
        #self.chronometer = Chronometer(stdscr)

        self.grid = Grid(stdscr, save)
        self.food = Food(stdscr, save)
        self.snake = Snake(stdscr, save, self.grid, self.food)


    def start(self):

        while True:
            self.grid.display()
            #self.chronometer.display()
            #self.food.display()
            #self.snake.display()

            self.key = self.stdscr.getch()

            if self.key == ord('q'):
                return
            elif self.key == ord('p'):
                '''
                Pausar el ciclo del juego
                '''
                self.menu.deploy(pause_menu)
                if self.menu.key_pressed == 1: continue
                elif self.menu.key_pressed == 2: return
            #elif self.key in self.snake.movement_keys:
            #    self.snake.move(self.key)
            #    self.food.check(self.snake.location)


'''
Tengo que hacer dentro de el mismo Game.py, dentro de la propia clase Game,
una función que se ejecute en otro thread y que cumpla dos funciones a la vez,
una es la de actualizar el cronómetro y la otra es la de mover la serpiente cada
cierto tiempo, dependiendo de la dificultad.

Quiero que todo sea manejado como un solo cronometro desde el que se pueda pausar 
y reanudar, y que al pausar se pause tanto el cronómetro como el movimiento de 
la serpiente.
'''