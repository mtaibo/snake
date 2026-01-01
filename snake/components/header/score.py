import reflex as rx
from snake.state import State
from snake.styles.components.header import score_style

def score() -> rx.Component:

    return rx.hstack(
        rx.text('SCORE'),
        rx.text('00'),
        style={
            **score_style, 
            'display': rx.cond(
                State.game_status == 'stopped', 
                'none', 
                'flex'
            )            
        }
    )