import reflex as rx
from snake.styles.styles import score_style


def score() -> rx.Component:

    return rx.hstack(
        rx.text('SCORE'),
        rx.text('00'),
        style=score_style
    )