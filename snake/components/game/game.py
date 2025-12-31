import reflex as rx


def game() -> rx.Component:

    return rx.box(
        rx.text('GameBoard')
    )