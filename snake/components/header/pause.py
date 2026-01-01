import reflex as rx
from snake.styles.styles import pause_style


def pause() -> rx.Component:

    return rx.button(
        rx.hstack(
            rx.image(
                src='/icons/pause_button.svg',
                width='30px', 
                height='30px',
            ),
            rx.text(
                'PAUSE',
                font_size='20px',
            ),
            style={
                'display' : 'flex',
                'align-items' : 'center',
                'justify-content' : 'center',
            }
        ),
        style=pause_style
    )