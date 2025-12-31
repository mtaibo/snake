import reflex as rx

from snake.styles.styles import *
from snake.styles.colors import *


def board_area():

    return rx.box(
        rx.box(
            width="min(70vh, 700px)",
            aspect_ratio="1",
            background="#5a5a5a",
            border=f"1px solid {BORDER}",
            border_radius="18px",
            box_shadow="0 10px 30px rgba(0,0,0,0.35)",
        ),
        rx.text(
            "Arrow keys / WASD to move · Space to pause · R to restart",
            opacity=0.7,
            font_size="13px",
            margin_top="10px",
            text_align="center",
        ),
        flex="1",
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        min_width="0px",
    )
