import reflex as rx
from snake.styles.styles import pause_style


def pause() -> rx.Component:

    return rx.button(
        'PAUSE',
        style=pause_style
    )