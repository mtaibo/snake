import reflex as rx


def score() -> rx.Component:

    return rx.hstack(
        rx.text('SCORE'),
        rx.text('00'),
    )