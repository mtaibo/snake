import reflex as rx


def left_sidebar() -> rx.Component:

    return rx.vstack(
        rx.text('Settings')
    )


def left_sidebar_shown() -> rx.Component:

    return rx.vstack(
        rx.text('Settings')
    )


def left_sidebar_hidden() -> rx.Component:

    return rx.vstack(
        rx.text('None')
    )