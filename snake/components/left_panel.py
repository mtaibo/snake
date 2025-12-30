import reflex as rx

from snake.styles.styles import *
from snake.styles.colors import *


def left_panel(State):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("Controls", weight="bold"),
                rx.spacer(),
                rx.button(
                    "Hide",
                    size="2",
                    on_click=State.toggle_panel,
                ),
                width="100%",
                align="center",
            ),
            rx.divider(),
            rx.text("Move: Arrow keys / WASD", opacity=0.85),
            rx.text("Pause: Space", opacity=0.85),
            rx.text("Restart: R", opacity=0.85),
            rx.divider(),
            rx.text("Settings", weight="bold"),
            rx.text("Speed / Grid size / Sound...", opacity=0.85),
            spacing="3",
            width="100%",
        ),
        width="320px",
        padding="16px",
        border=f"1px solid {BORDER}",
        border_radius="16px",
        background=CARD,
        box_shadow="0 10px 30px rgba(0,0,0,0.20)",
    )


