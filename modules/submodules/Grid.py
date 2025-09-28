# Import standard libraries
import curses


class Grid():
    def __init__(self, stdscr):

        self.stdscr = stdscr

        # Customizable grid options
        self.height_percentage = 70
        self.width_percentage = 40

        # Non customizable grid options
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        self.height = round(self.screen_height * self.height_percentage/100)
        self.width = round(self.screen_width * self.width_percentage/100) 
        self.grid_top_left_corner_height = round((self.screen_height // 2) - (self.height // 2))
        self.grid_top_left_corner_width = round((self.screen_width // 2) - ((self.width) // 2))

        # Controls and characters
        self.controls = 'W/A/S/D'
        self.characters = {
            'top_bottom' : '═',
            'left_right' : '║',
            'corner_left_top' : '╔',
            'corner_right_top' : '╗',
            'corner_left_bottom' : '╚',
            'corner_right_bottom' : '╝',
        }

    def countdown(self):
        
        # Countdown before the game
        for i in range(3, 0, -1):
            self.stdscr.addstr(self.screen_height//2, (self.screen_width//2)-1, str(i))
            self.stdscr.refresh()
            curses.napms(600)
            self.stdscr.clear()


    def display(self):
        
        # Imprimir algunos parámetros del juego
        self.stdscr.addstr(0, 0, 'Height: {} , Width {}'.format(self.height, self.width))

        # Imprimir la línea superior del mapa
        self.stdscr.addstr(self.grid_top_left_corner_height-1, 
                           self.grid_top_left_corner_width-1,
                           '{}{}{}'.format(
                                self.characters['corner_left_top'],
                                self.characters['top_bottom'] * (self.width),
                                self.characters['corner_right_top']))

        # Imprimir la superficie del mapa
        for i in range(self.height):
            line = ''
            for j in range(self.width+2): # +2 for the edges
                if j == 0: line += self.characters['left_right']
                elif j == self.width+1: line += self.characters['left_right']
                else: line += ' '
            self.stdscr.addstr(self.grid_top_left_corner_height+i,
                               self.grid_top_left_corner_width-1, line)

        # Imprimir la línea inferior del mapa
        self.stdscr.addstr(self.grid_top_left_corner_height+self.height, 
                           self.grid_top_left_corner_width-1,
                           '{}{}{}'.format(
                                self.characters['corner_left_bottom'],
                                self.characters['top_bottom'] * (self.width),
                                self.characters['corner_right_bottom']))

        # Imprimir los elementos de la parte superior e inferior
        self.stdscr.addstr(self.grid_top_left_corner_height-2,
                           self.grid_top_left_corner_width, '[Q] Quit [P] Pause')
        self.stdscr.addstr(self.grid_top_left_corner_height+self.height+1,
                           self.grid_top_left_corner_width, f'{self.controls} :')

        # Aplicar los cambios a la pantalla
        self.stdscr.refresh()