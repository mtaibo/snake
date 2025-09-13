# Import interface library
import curses

# Import script modules
from modules.Save import Save
from modules.Menu import Menu
from modules.Game import Game

# Import menu templates
from templates.menus import *


def main(stdscr):

    curses.curs_set(0) # Hide the cursor

    save = Save()
    menu = Menu(stdscr, save)
    game = Game(stdscr, save)

    while True:
        menu.deploy(main_menu)

        if menu.key_pressed == 1: game.start() 
        elif menu.key_pressed == 2: menu.deploy(settings_menu)
        elif menu.key_pressed == 3: menu.deploy(high_scores_menu)
        elif menu.key_pressed == 4: menu.deploy(about_menu)
        elif menu.key_pressed == 5: break

    save.save_file(save.file)


if __name__ == "__main__":
    curses.wrapper(main)