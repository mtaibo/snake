import reflex as rx
from snake.components.game.start import start


def game() -> rx.Component:

    return rx.box(
        start(),
        rx.text('GameBoard'),
    )