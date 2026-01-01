import reflex as rx
from snake.styles.components.header import title_style

def title() -> rx.Component:

    return rx.heading(
        'SNAKE',
        style=title_style
    )