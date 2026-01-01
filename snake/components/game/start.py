import reflex as rx
from snake.styles.styles import start_style, soft_text


def start() -> rx.Component:

    return rx.button(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src='/icons/play_button.svg',
                    width='30px', 
                    height='30px'
                ),
                rx.text('START'),
                style={
                    'display' : 'flex',
                    'align-items' : 'center',
                    'justify-content' : 'center',
                }
            ),
            rx.text(
                'Click/Space to start',
                style=soft_text
            ),
        ),
        style=start_style
    )