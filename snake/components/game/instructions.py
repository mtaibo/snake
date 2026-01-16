import reflex as rx
from snake.state import State

from snake.styles.components.game import *
from snake.components.game.start import start


def instructions() -> rx.Component:

    return rx.text(
        'Arrow keys / WASD to move · Space to pause · R to restart',
        style=instructions_style
    )