import reflex as rx
from rxconfig import *
from snake.state import State    

# Style files
from snake.styles.styles import *
from snake.styles.layout import *

# Header components
from snake.components.header.title import title
from snake.components.header.score import score
from snake.components.header.pause import pause

# Page content components
from snake.components.sidebars.left_sidebar import left_sidebar
from snake.components.sidebars.right_sidebar import right_sidebar
from snake.components.game.game import game


def index() -> rx.Component:

    return rx.vstack(

        # Header
        rx.hstack(
            title(),
            rx.hstack(
                score(),
                pause(),
                style=mid_header_style
            ),
            style=header_style
        ),

        # Content
        rx.hstack(
            left_sidebar(),
            game(), 
            right_sidebar(),
            style=content_style
        ),

        style=base_style
    )

app = rx.App(head_components=head)
app.add_page(index, route="/", title="Snake")
