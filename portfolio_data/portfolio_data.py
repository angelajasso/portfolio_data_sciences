import reflex as rx

class MyState(rx.State):
    accent = "#F7ABA1"
    bg_color = "#FCD4CF"
    black = "#1C1817"
    white = "#FEE9E6"

def header():
    return rx.hstack(
        rx.image(
            src="Logo.svg",
            margin="16px",
        ),
        
        rx.el.h1(
            "Angela Jasso",
            font_size="1.5rem",
            color=MyState.black
        ),
        width="calc(100% - 2rem)",
        height="80px",
        background_color=MyState.bg_color,
        spacing="4",
        border_radius="20px",
        margin="1rem",
        align="center",
    )
    
def hero():
    return rx.box(
        rx.el.h2(
            "Data Scientist | Python Enthusiast 🐍",
            font_size="2.4rem",
            color=MyState.black,
            margin="32px",
            text_align="center",
        ),
        border_radius="20px",
        display="flex",
        justify_content="center",
        align_items="center",
        height="30rem",
        width="calc(100% - 2rem)",  # O ajusta el valor según el margen deseado
        margin="0 1rem",  # Espacio alrededor
        background=MyState.bg_color,
    )
    
def photo():
    return rx.box(
        rx.image(
            src="descarga.png",
            width="300px", 
            height="400px",
            border_radius="150px",
        ),
        border_radius="20px",
        display="flex",
        justify_content="center",
        align_items="center",
        height="30rem",
        width="calc(100% - 2rem)",  # O ajusta el valor según el margen deseado
        margin="1rem",  # Espacio alrededor
        background=MyState.bg_color,
    )
    
    
def about():
    return rx.box(
        rx.el.p(
            "Angela Jasso turns data into stories and numbers into decisions. 🚀 With experience in machine learning, data analysis, and visualization, she uses tools like Pandas, Scikit-learn, and NumPy to create impact. 🔍📈",
            font_size="1rem",
            color=MyState.black,
            margin="16px",
            text_align="center",
        ),
        border_radius="20px",
        display="flex",
        justify_content="center",
        align_items="center",
        height="30rem",
        width="calc(100% - 2rem)",  # O ajusta el valor según el margen deseado
        margin="1rem",  # Espacio alrededor
        background=MyState.bg_color,
    )

def projects():
    return rx.box(
        rx.flex(
            rx.el.p(
                "Musea",
                font_size="1rem",
                color=MyState.black,
                margin="16px",
                text_align="center",
            ),
            rx.icon(
                "move-up-right", 
                size=18, 
                color=MyState.accent,
            ),
                
            direction="row",
            gap="4",
            align="center",
            ),
        rx.divider(
            size="4", 
            color_scheme="ruby"
        ),
        rx.flex(
            rx.el.p(
                "Musea",
                font_size="1rem",
                color=MyState.black,
                margin="16px",
                text_align="center",
            ),
            rx.icon(
                "move-up-right", 
                size=18, 
                color=MyState.accent,
            ),
                
            direction="row",
            gap="4",
            align="center",
            ),
        rx.divider(size="4", color_scheme="ruby"),
        rx.flex(
            rx.el.p(
                "Musea",
                font_size="1rem",
                color=MyState.black,
                margin="16px",
                text_align="center",
            ),
            rx.icon(
                "move-up-right", 
                size=18, 
                color=MyState.accent,
            ),
                
            direction="row",
            gap="4",
            align="center",
        ),
        rx.divider(size="4", color_scheme="ruby"),
        rx.flex(
            rx.el.p(
                "Musea",
                font_size="1rem",
                color=MyState.black,
                margin="16px",
                text_align="center",
            ),
            rx.icon(
                "move-up-right", 
                size=18, 
                color=MyState.accent,
            ),
                
            direction="row",
            gap="4",
            align="center",
        ),
        spacing="4",
        direction="column",
        align="center",
        border_radius="20px",
        margin="0 8px",
        width="95%",
        height="auto",
        background=MyState.bg_color,
    )
    
def footer():
    return rx.hstack(
        rx.link(
            "GitHub", 
            href="https://reflex.dev/",
            color=MyState.white,
        ),
        rx.link(
            "Kaggle", 
            href="https://reflex.dev/",
            color=MyState.white,
        ),
        font_size="1rem",
        color=MyState.black,
        width="95%",
        height="80px",
        background_color=MyState.accent,
        spacing="4",
        border_radius="20px",
        margin="8px",
        display="flex",
        justify_content="center",
        align_items="center",
    )

def index():
    return rx.grid(
        rx.box(header(), grid_area="header"),
        rx.box(hero(), style={"grid_column": "1", "grid_row": "2"}),
        rx.box(photo(), style={"grid_column": "2", "grid_row": "2"}),
        rx.box(about(), grid_area="about"),
        rx.box(projects(), grid_area="projects"),
        rx.box(footer(), grid_area="footer"),
        columns="1",  # Mobile First: 1 columna base
        background_color=MyState.white,
        spacing="4",
        justify="center",
        align="center",
        
        style={
            "grid_template_areas": """  
                'header'  
                'hero'  
                'photo'  
                'about'  
                'projects'  
                'footer'  
            """,  # Diseño base (móviles)
            "media_queries": {
                "(min-width: 650px)": {  
                    "columns": "2",
                    "width": "90%",
                    "grid_column_gap": "1rem",
                    "grid_row_gap": "1rem",
                    "grid_template_areas": """  
                        'header  header'  
                        'hero    photo'  
                        'about   about'  
                        'projects projects'  
                        'footer  footer'  
                    """,
                },
                "(min-width: 1024px)": {  
                    "columns": "3",
                    "grid_template_rows": "auto",
                    "width": "80%",
                    "font_size": "24px",
                    "grid_template_areas": """  
                        'header   header   header'  
                        'hero     photo    projects'  
                        'about    about    projects'  
                        'footer   footer   footer'  
                    """,
                },
            },
        },
    )


app = rx.App()
app.add_page(index)