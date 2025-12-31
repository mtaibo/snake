import reflex as rx
from rxconfig import config

from snake.styles.styles import *
from snake.styles.colors import * 

from snake.components.left_panel import left_panel
from snake.components.board_area import board_area


class State(rx.State):
    panel_open: bool = True
    score: int = 0
    high: int = 12
    status: str = "PAUSED"

    def toggle_panel(self):
        self.panel_open = not self.panel_open


def index():
    return rx.box(
        rx.vstack(
            # Header
            rx.hstack(
                rx.heading("SNAKE", size="9", weight="bold"),
                rx.spacer(),
                # Botón para reabrir el panel cuando está oculto
                rx.cond(
                    State.panel_open,
                    rx.box(),  # nada cuando está abierto (ya tienes Hide dentro del panel)
                    rx.button("Show controls", size="2", on_click=State.toggle_panel),
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text("SCORE", opacity=0.7, font_size="12px"),
                        rx.text(
                            rx.cond(
                                State.score < 10,
                                "00" + State.score.to_string(),
                                rx.cond(
                                    State.score < 100,
                                    "0" + State.score.to_string(),
                                    State.score.to_string(),
                                ),
                            ),
                            font_size="24px",
                            weight="bold",
                        ),
                        spacing="1",
                        align="end",
                    ),
                    rx.vstack(
                        rx.text("HIGH", opacity=0.7, font_size="12px"),
                        rx.text(
                            rx.cond(
                                State.score < 10,
                                "00" + State.score.to_string(),
                                rx.cond(
                                    State.score < 100,
                                    "0" + State.score.to_string(),
                                    State.score.to_string(),
                                ),
                            ),
                            font_size="24px",
                            weight="bold",
                        ),
                        spacing="1",
                        align="end",
                    ),
                    rx.badge(State.status, variant="solid"),
                    spacing="6",
                    align="center",
                ),
                width="100%",
                align="center",
            ),

            # Main
            rx.hstack(
                # Panel izquierdo condicional
                rx.cond(
                    State.panel_open,
                    left_panel(State),
                    rx.box(width="0px"),  # placeholder (evita rarezas de layout)
                ),

                board_area(),
                spacing="6",
                width="100%",
                align="start",
            ),

            spacing="6",
            width="100%",
        ),
        min_height="100vh",
        padding=["20px", "24px", "48px"],
        background=BG,
        color="white",
    )


app = rx.App(
    head_components=head
)

app.add_page(index, route="/", title="Snake")
