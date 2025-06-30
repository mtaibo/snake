import curses

# Import save module
from modules.Save import Save

# Import menu module and menus templates
from modules.Menu import Menu
from templates.menus import *


def main(stdscr):

    save = Save()
    menu = Menu(stdscr)

    while True:
        menu.deploy(main_menu)

        if menu.key_pressed == 1:
            break
        elif menu.key_pressed == 2:
            menu.deploy(settings_menu)
        elif menu.key_pressed == 3:
            menu.deploy(high_scores_menu)
        elif menu.key_pressed == 4:
            menu.deploy(about_menu)
        elif menu.key_pressed == 5:
            break

    save.save_file(save.file)

if __name__ == "__main__":
    curses.wrapper(main)