import reflex as rx
from snake.state import State

from snake.styles.components.buttons import start_style
from snake.styles.typography import SOFT_TEXT
from snake.styles.mixins import FLEX_CENTER
from snake.styles.measures import BUTTON_ICONS

def start() -> rx.Component:

    return rx.button(
        rx.vstack(
            rx.hstack(
                rx.image(src='/icons/play_button.svg', style=BUTTON_ICONS),
                rx.text('START'),
                style=FLEX_CENTER
            ),
            rx.text(
                'Click/Space to start',
                style=SOFT_TEXT
            ),
        ),

        # Action that this button triggers
        on_click=State.start,

        # This style contains the pause_style and adds a rx.cond 
        # to show this button only for game_status 'playing'
        style={
            **start_style, 
            'display': rx.cond(
                State.game_status == 'stopped',
                'flex', 
                'none'
            )            
        }
    )