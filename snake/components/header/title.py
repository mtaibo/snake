import reflex as rx
from snake.styles.styles import heading


def title() -> rx.Component:

    return rx.heading(
        'SNAKE',
        style=heading
    )