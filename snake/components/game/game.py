import reflex as rx
from snake.state import State, GameStatus

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
                    State.game_status == GameStatus.STOPPED,
                    'none', 
                    'block'
                )            
            }
        )
    )