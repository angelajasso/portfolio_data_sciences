import reflex as rx

def header():
    return rx.hstack(
        rx.image(src="../assets/Logo.svg"),
        rx.el.h2(
            "Angela Jasso",
            font_size="1.6rem",
            color="#1C1817",
        ),
        width="100%",
        background_color="#FCD4CF",
        spacing="4",
        border_radius="20px",
    )

def index():
    return rx.vstack(
        header(),
        background_color="#FEE9E6",
        spacing="4",
    )

app = rx.App()
app.add_page(index)