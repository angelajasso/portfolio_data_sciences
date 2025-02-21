import reflex as rx

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="ruby",
        ),
        rx.heading(font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="grass",
        ),
        spacing="4",
    )

app = rx.App()
app.add_page(index)