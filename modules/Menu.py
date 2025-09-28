import threading
import curses
import time


class Menu():
    def __init__(self, stdscr, save=None):
        self.menu = ""
        self.stdscr = stdscr
        self.save = save

    def deploy(self, menu):

        self.menu = menu
        self.menu_setup() # Prepare the self variables for the menu printing

        while True:
            # Print the menu
            self.stdscr.clear()
            for index, line in enumerate(self.menu): self.stdscr.addstr(self.screen_center_y+index, self.screen_center_x, line)

            # Print the invalid key message
            if self.key_pressed not in self.available_options and self.key_pressed not in (None, -1):
                self.warning_message('Invalid option!')

            self.stdscr.refresh()
            
            # Get the user input
            self.key_pressed = self.stdscr.getch()

            if self.key_pressed in self.available_options:
                self.key_pressed = int(chr(self.key_pressed))
                for index, line in enumerate(self.menu): self.stdscr.addstr(self.screen_center_y+index, self.screen_center_x, " "*len(line))
                return
            elif self.available_options == [] and self.key_pressed:
                for index, line in enumerate(self.menu): self.stdscr.addstr(self.screen_center_y+index, self.screen_center_x, " "*len(line))
                return

    
    def menu_setup(self):

        # Find if the menu has {} to format it with the save data
        if '{}' in self.menu:
            if 'settings' in self.menu.lower(): self.menu = self.menu.format(*self.save.settings_format)
            elif 'high scores' in self.menu.lower(): self.menu = self.menu.format(self.save.high_scores_format)

        self.menu = self.menu.split("\n")

        # Set empty variables
        self.key_pressed = None
        self.longest_lines = []
        self.available_options = []

        # Get screen size
        screen_height, screen_width = self.stdscr.getmaxyx()
        # Get the menu size
        self.menu_height = len(self.menu)
        self.menu_width = max(len(line) for line in self.menu)
        # Get the center of the screen
        self.screen_center_y = (screen_height // 2) - (self.menu_height // 2)
        self.screen_center_x = (screen_width // 2) - (self.menu_width // 2) # Longest line

        # Get the index on the menu list of the longest lines
        for i, line in enumerate(self.menu):
            if '===' in line: self.longest_lines.append(i)
        # Get the available options
        number = 1
        available_options = []
        for i, line in enumerate(self.menu):
            if len(line) > 1 and line[0] == str(number) and line[1] == ".": 
                available_options.append(number)
                number += 1
        if len(available_options) > 0:
            for n in range(len(available_options)): self.available_options.append(49+n)

        # Set the colors
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.COLOR_RED = curses.color_pair(1)


    def warning_message(self, message):

        y, x = self.stdscr.getyx()
        
        def temporal_delete():
            time.sleep(3)
            self.stdscr.addstr(y+3,x-len(self.menu[-1]), " "*len(message))
            self.stdscr.move(y, x)
            self.stdscr.refresh()
        
        self.stdscr.addstr(y+3,x-len(self.menu[-1]), message, self.COLOR_RED | curses.A_BLINK)
        threading.Thread(target=temporal_delete, daemon=True).start()

        self.stdscr.move(y, x)