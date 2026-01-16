import reflex as rx
from snake.state import State

from snake.styles.components.game import *
from snake.components.game.start import start

def game() -> rx.Component:

    return rx.box(
        start(),
        rx.el.canvas(
            id='game-canvas',
            style={
                **canvas_style, 
                'display': rx.cond(
                    State.game_status == 'stopped',
                    'none', 
                    'block'
                )            
            }
        )
    )