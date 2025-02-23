import reflex as rx

def header():
    return rx.hstack(
        rx.html(
            '<svg width="52" height="51" viewBox="0 0 52 51" fill="none" xmlns="http://www.w3.org/2000/svg">'
            '<circle cx="24" cy="24" r="24" fill="#F7ABA1"/>'
            '<circle cx="28" cy="27" r="23" fill="#FEE9E6" stroke="#F7ABA1" stroke-width="2"/>'
            '<path fill-rule="evenodd" clip-rule="evenodd" d="M41 16.7949C41 18.6399 40.3421 20.3352 39.2425 21.6702C43.5486 21.7951 47 25.2356 47 29.4615C47 33.7665 43.4183 37.2564 39 37.2564C37.7423 37.2564 36.5524 36.9736 35.4936 36.4697C35.821 37.3209 36 38.2426 36 39.2051C36 43.5101 32.4183 47 28 47C23.7206 47 20.2261 43.7261 20.0105 39.6087C19.0813 39.9767 18.0649 40.1795 17 40.1795C12.5817 40.1795 9 36.6896 9 32.3846C9 28.7503 11.5527 25.6969 15.0063 24.8337C13.1738 23.4053 12 21.208 12 18.7436C12 14.4386 15.5817 10.9487 20 10.9487C22.286 10.9487 24.3481 11.883 25.806 13.381C27.105 10.7871 29.8383 9 33 9C37.4183 9 41 12.4899 41 16.7949Z" fill="#F7ABA1"/>'
            '<path d="M18.16 32L22.176 21.296H23.856L27.856 32H26.256L25.44 29.664H20.576L19.76 32H18.16ZM21.04 28.368H24.976L23.008 22.816L21.04 28.368ZM31.5996 32.192C30.597 32.192 29.8023 31.9253 29.2156 31.392C28.629 30.848 28.309 30.0427 28.2556 28.976L29.6476 28.576C29.6263 29.3867 29.813 29.9893 30.2076 30.384C30.6023 30.768 31.0663 30.96 31.5996 30.96C31.8876 30.96 32.1756 30.896 32.4636 30.768C32.7516 30.64 32.9863 30.4053 33.1676 30.064C33.3596 29.7227 33.4556 29.232 33.4556 28.592V21.312H34.9596V28.608C34.9596 29.7707 34.661 30.6613 34.0636 31.28C33.4663 31.888 32.645 32.192 31.5996 32.192Z" fill="#FEE9E6"/>'
            '</svg>',
            margin="16px",
        ),
        
        rx.el.h2(
            "Angela Jasso",
            font_size="1.6rem",
            color="#1C1817",
        ),
        width="99%",
        height="auto",
        background_color="#FCD4CF",
        spacing="4",
        border_radius="20px",
        margin="4px",
        align="center",
    )

def index():
    return rx.vstack(
        header(),
        background_color="#FEE9E6",
        spacing="4",
        justify="center",
        style={
            "media_queries": {
                "(min-width: 768px)": {  # Tablets y más grandes
                    "flex_direction": "row",  # En pantallas grandes, cambia a fila
                    "justify_content": "center",
                },
                "(min-width: 1024px)": {  # Desktop
                    "font_size": "24px",
                    "width": "80%",
                },
            }
        }
    )

app = rx.App()
app.add_page(index)