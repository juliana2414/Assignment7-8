import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.YETI], use_pages=True)
server = app.server

app.layout = dbc.Container(
    children=[
        dbc.NavbarSimple(
            brand="Car Dashboard",
            children=[
                dbc.NavItem(dbc.NavLink("My Main Dashboard", href='/')),
                dbc.NavItem(dbc.NavLink("Second Page", href='/page2')),
            ],
            color="info",
            dark=True,
        ),
        dash.page_container,
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
