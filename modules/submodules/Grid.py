

class Grid():
    def __init__(self, stdscr, save):
        self.stdscr = stdscr
        self.height_percentage = 70
        self.width_percentage = 50
        self.characters = {
            'top_bottom' : '═',
            'left_right' : '║',
            'corner_left_top' : '╔',
            'corner_right_top' : '╗',
            'corner_left_bottom' : '╚',
            'corner_right_bottom' : '╝',
        }
        screen_height, screen_width = self.stdscr.getmaxyx()
        self.height = round(screen_height * self.height_percentage/100)
        self.width = round(screen_width * self.width_percentage/100)

        self.screen_center_height = (screen_height // 2) - (self.height // 2)
        self.screen_center_width = (screen_width // 2) - ((self.width + 2) // 2)

    def display(self):
        
        self.stdscr.clear()

        # Imprimir la línea superior del mapa
        self.stdscr.addstr(round(self.screen_center_height), 
                        round(self.screen_center_width),
                        '{}{}{}'.format(
                            self.characters['corner_left_top'],
                            f'{self.characters['top_bottom'] * self.width}',
                            self.characters['corner_right_top'],
                        ))

        # Imprimir la superficie del mapa

        for i in range(self.height):
            line = ''
            for j in range(self.width+2):
                if j == 0: line += self.characters['left_right']
                elif j == self.width+1: line += self.characters['left_right']
                else: line += ' '
            self.stdscr.addstr(self.screen_center_height+i+1,
                            self.screen_center_width, line)

        # Imprimir la línea inferior del mapa
        self.stdscr.addstr(round(self.screen_center_height+self.height), 
                round(self.screen_center_width),
                '{}{}{}'.format(
                    self.characters['corner_left_bottom'],
                    f'{self.characters['top_bottom'] * self.width}',
                    self.characters['corner_right_bottom'],
                ))

        # Imprimir los controles en la parte superior e inferior
        self.stdscr.addstr(self.screen_center_height-2,
                        self.screen_center_width,
                        '[Q] Quit [P] Pause')
        self.stdscr.addstr(self.screen_center_height+self.height+2,
                        self.screen_center_width,
                        'W/A/S/D : ')
        self.stdscr.refresh()