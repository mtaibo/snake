import reflex as rx
from rxconfig import *

# Style files
from snake.styles.styles import *
from snake.styles.colors import * 

# Header components
from snake.components.header.title import title
from snake.components.header.score import score
from snake.components.header.pause import pause

# Page content components
from snake.components.sidebars.left_sidebar import left_sidebar
from snake.components.sidebars.right_sidebar import right_sidebar
from snake.components.game.start import start
from snake.components.game.game import game



class State(rx.State):
    pass


def index():

    return rx.vstack(

        # Header

        rx.hstack(
            title(),
            score(),
            pause(),
        ),

        # Page Content

        rx.hstack(
            left_sidebar(),
            start(),
            game(), 
            right_sidebar(),
        )
    )


app = rx.App(
    head_components=head
)

app.add_page(index, route="/", title="Snake")
