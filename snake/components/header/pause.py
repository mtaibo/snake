import reflex as rx
from snake.state import State

from snake.styles.components.buttons import pause_style
from snake.styles.mixins import FLEX_CENTER
from snake.styles.measures import BUTTON_ICONS

def pause() -> rx.Component:

    return rx.button(
        
        # Depending on the game_status, this button will
        # work as a Pause or a Play button
        rx.cond(
            State.game_status == 'playing',
            rx.hstack(
                rx.image(src='/icons/pause_button.svg', style=BUTTON_ICONS),
                rx.text('PAUSE', width='4.7vw',font_size='20px'),
                style=FLEX_CENTER,
            ),
            rx.hstack(
                rx.image(src='/icons/play_button.svg', style=BUTTON_ICONS),
                rx.text('PLAY', width='4.7vw', font_size="20px"),
                style=FLEX_CENTER,
            ),
        ),

        # Action that this button triggers
        on_click=State.pause_resume,

        # This style contains the pause_style and adds a rx.cond 
        # to show this button only for game_status 'playing'
        style={
            **pause_style, 
            'display': rx.cond(
                State.game_status == 'stopped', 
                'none', 
                'flex'
            )            
        }
    )