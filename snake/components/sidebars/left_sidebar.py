import reflex as rx
from snake.state import State

from snake.styles.styles import sidebar_shown_style, left_sidebar_hidden_style, sidebar_toggle, sidebar_text


def left_sidebar() -> rx.Component:
    return rx.cond(State.left_open, left_sidebar_shown(), left_sidebar_hidden())

def left_sidebar_shown() -> rx.Component:

    return rx.vstack(
        rx.text(
            'Settings',
            style=sidebar_text
        ),
        rx.button(
            rx.icon(tag="chevron_left"),
            on_click=State.toggle_left,
            style=sidebar_toggle
        ),
        style=sidebar_shown_style
    )

def left_sidebar_hidden() -> rx.Component:

    return rx.vstack(
        rx.button(
            rx.icon(tag="chevron_right"),
            on_click=State.toggle_left,
            style=sidebar_toggle
        ),
        style=left_sidebar_hidden_style
    )