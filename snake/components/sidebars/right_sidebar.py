import reflex as rx
from snake.state import State
from snake.styles.colors import *

from snake.styles.styles import sidebar_shown_style, right_sidebar_hidden_style, sidebar_text, sidebar_toggle


'''
def right_sidebar() -> rx.Component:
    return rx.cond(State.right_open, right_sidebar_shown(), right_sidebar_hidden())
'''

def right_sidebar_shown() -> rx.Component:

    return rx.vstack(
        rx.button(
            rx.icon(tag="chevron_right"),
            on_click=State.toggle_right,
            style=sidebar_toggle
        ),
        rx.text(
            'Leaderboard',
            style=sidebar_text
        ),
        style=sidebar_shown_style
    )

def right_sidebar_hidden() -> rx.Component:

    return rx.vstack(
        rx.button(
            rx.icon(tag="chevron_left"),
            on_click=State.toggle_right,
            style=sidebar_toggle
        ),
        style=right_sidebar_hidden_style
    )

SIDEBAR_W = "19vw"   # ancho del “slot” del sidebar (ajústalo)
SIDEBAR_H = "60vh"   # lo que dijiste que fijaste
RAIL_W    = "50px"   # ancho visible cuando está “cerrado”

def right_sidebar() -> rx.Component:
    return rx.box(
        # Panel completo que se mueve
        rx.box(
            # Rail (siempre visible)
            rx.box(
                rx.button(
                    rx.cond(
                        State.right_open,
                        rx.icon(tag="chevron_right", width='20px',height='20px'),  # abierto: sugiere “cerrar”
                        rx.icon(tag="chevron_left", width='20px',height='20px'),   # cerrado: sugiere “abrir”
                    ),
                    on_click=State.toggle_right,
                    width=RAIL_W,
                    height='100%',
                    border_radius='25px',
                    background_color=SECONDARY,
                    _hover={
                        'cursor' : 'pointer'
                    }
                ),
                position="absolute",
                left="0",
                top="0",
                width=RAIL_W,
                height="100%",
                display="flex",
                align_items="center",
                justify_content="center",
            ),

            # Contenido (se “va” con el panel al cerrar)
            rx.vstack(
                rx.text("Leaderboard", font_weight="700"),
                width="100%",
                padding="16px",
                padding_left=f"calc({RAIL_W} + 16px)",  # deja hueco para la rail
                opacity=rx.cond(State.right_open, "1", "0"),
                transition="opacity 120ms ease",
                pointer_events=rx.cond(State.right_open, "auto", "none"),
            ),

            # Estilo del panel
            width="100%",
            height="100%",
            position="relative",
            border_radius="16px",
            box_shadow="0 8px 24px rgba(0,0,0,0.18)",
            background_color=SECONDARY,

            # Movimiento: cerrado => se desplaza a la izquierda dejando solo la rail dentro del slot
            transform=rx.cond(
                State.right_open,
                "translateX(0)",
                f"translateX(calc(100% + {'20px'}))",
            ),
            transition="transform 300ms ease",
        ),

        # Slot del sidebar (en tu grid de 3 columnas)
        width=SIDEBAR_W,
        height=SIDEBAR_H,
        justify_self="start",  # el sidebar “nace” pegado al borde izquierdo de su columna (junto al canvas)
        overflow="visible",    # el panel se mueve; no lo recortes aquí
    )