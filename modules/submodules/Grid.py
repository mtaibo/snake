import curses


class Grid():
    def __init__(self, stdscr):
        self.stdscr = stdscr

        # Customizable grid options
        self.height_percentage = 70
        self.width_percentage = 40

        # Non customizable grid options
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        self.height = round(self.screen_height * self.height_percentage/100) ### 24
        self.width = round(self.screen_width * self.width_percentage/100) ### 48
        self.screen_center_height = round((self.screen_height // 2) - (self.height // 2))
        self.screen_center_width = round((self.screen_width // 2) - ((self.width) // 2))

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


    def display(self):
        
        # Countdown before starting the game
        for i in range(3, 0, -1):
            self.stdscr.addstr(self.screen_height//2, (self.screen_width//2)-1, str(i))
            self.stdscr.refresh()
            curses.napms(600)
            self.stdscr.clear()

        # Imprimir algunos parámetros del juego
        self.stdscr.addstr(0, 0, 'Height: {} , Width {}'.format(self.height, self.width))

        # Imprimir la línea superior del mapa
        self.stdscr.addstr(self.screen_center_height, 
                           self.screen_center_width,
                           '{}{}{}'.format(
                                self.characters['corner_left_top'],
                                self.characters['top_bottom'] * self.width,
                                self.characters['corner_right_top']))

        # Imprimir la superficie del mapa
        for i in range(self.height):
            line = ''
            for j in range(self.width+2): # +2 for the left and right borders
                if j == 0: line += self.characters['left_right']
                elif j == self.width+1: line += self.characters['left_right']
                else: line += ' '
            self.stdscr.addstr(self.screen_center_height+1+i,
                               self.screen_center_width, line)

        # Imprimir la línea inferior del mapa
        self.stdscr.addstr(self.screen_center_height+self.height, 
                           self.screen_center_width,
                           '{}{}{}'.format(
                                self.characters['corner_left_bottom'],
                                self.characters['top_bottom'] * self.width,
                                self.characters['corner_right_bottom']))

        # Imprimir los elementos de la parte superior e inferior
        self.stdscr.addstr(self.screen_center_height-2,
                           self.screen_center_width, '[Q] Quit [P] Pause')
        self.stdscr.addstr(self.screen_center_height+self.height+2,
                           self.screen_center_width, f'{self.controls} :')

        # Aplicar los cambios a la pantalla
        self.stdscr.refresh()