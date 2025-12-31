import reflex as rx

config = rx.Config(
    app_name="snake",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)

head = [
    rx.el.link(rel="icon", type="image/png", sizes="32x32", href="/favicon/favicon.png?v=1"),
    rx.el.link(rel="apple-touch-icon", sizes="180x180", href="/favicon/apple-touch-icon.png?v=1"),
    rx.el.link(rel="icon", href="/favicon/favicon.ico?v=1"),
]