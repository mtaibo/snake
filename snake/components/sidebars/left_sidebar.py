import reflex as rx
from snake.state import State

from snake.styles.components.sidebar import *


def left_sidebar() -> rx.Component:

    return rx.box(
        
        # Button to open/close the sidebar
        rx.button(
            rx.cond(
                State.left_open,
                rx.icon(tag="chevron_left", style=BUTTON_ICONS),  
                rx.icon(tag="chevron_right", style=BUTTON_ICONS),   
            ),
            right=0,
            on_click=State.toggle_left,
            style=sidebar_button
        ),
 
        # Contenido del sidebar
        rx.vstack(
            rx.text('Settings'),
            opacity=rx.cond(State.left_open, '1', '0'),
            pointer_events=rx.cond(State.left_open, 'auto', 'none'),
            style=sidebar_content
        ),

        # Movimiento hacia la izquierda
        transform=rx.cond(
            State.left_open,
            "translateX(0)",
            f"translateX(calc(-100% - {BUTTON_WIDTH}))",
        ),

        style=sidebar_style
    )