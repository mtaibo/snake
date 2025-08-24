import curses

# Import save module
from modules.Save import Save

# Import menu module and menus templates
from modules.Menu import Menu
from templates.menus import *

# Import game modules
from modules.Game import *

def main(stdscr):

    curses.curs_set(0)

    save = Save()
    menu = Menu(stdscr)
    game = Game(stdscr, save)

    while True:
        menu.deploy(main_menu)

        if menu.key_pressed == 1:
            if save.first_time == True: menu.deploy(first_time_menu)
            game.start() 
        elif menu.key_pressed == 2:
            menu.deploy(raw_settings_menu.format(*save.settings_format))
        elif menu.key_pressed == 3:
            menu.deploy(raw_high_scores_menu.format(save.high_scores_format))
        elif menu.key_pressed == 4:
            menu.deploy(about_menu)
        elif menu.key_pressed == 5:
            break

    save.save_file(save.file)


if __name__ == "__main__":
    curses.wrapper(main)