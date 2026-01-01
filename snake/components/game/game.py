import reflex as rx
from snake.styles.styles import canvas_style, instructions_style
from snake.components.game.start import start


def game() -> rx.Component:

    return rx.box(
        start(),
        rx.text(
            'Arrow keys / WASD to move · Space to pause · R to restart',
            style=instructions_style
        ),
        style=canvas_style
    )