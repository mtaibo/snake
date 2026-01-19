import reflex as rx
from snake.state import State

from snake.styles.components.sidebar import *


def right_sidebar() -> rx.Component:

    return rx.box(

        # Button to open/close the sidebar
        rx.button(
            rx.cond(
                State.right_sidebar_open,
                rx.icon(tag='chevron_right', style=BUTTON_ICONS),  
                rx.icon(tag='chevron_left', style=BUTTON_ICONS),  
            ),
            left=0,
            on_click=State.toggle_sidebar('right'),
            style=sidebar_button
        ),

        # Contenido del sidebar
        rx.vstack(
            rx.text('Leaderboard'),
            opacity=rx.cond(State.right_sidebar_open, '1', '0'),
            pointer_events=rx.cond(State.right_sidebar_open, 'auto', 'none'),
            style=sidebar_content
        ),

        # Movimiento hacia la izquierda
        transform=rx.cond(
            State.right_sidebar_open,
            'translateX(0)',
            f'translateX(calc(100% + {BUTTON_WIDTH}))',
        ),

        style=sidebar_style
    )