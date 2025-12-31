import reflex as rx


def right_sidebar() -> rx.Component:

    return rx.vstack(
        rx.text('Leaderboard')
    )


def right_sidebar_shown() -> rx.Component:

    return rx.vstack(
        rx.text('Leaderboard')
    )


def right_sidebar_hidden() -> rx.Component:

    return rx.vstack(
        rx.text('None')
    )