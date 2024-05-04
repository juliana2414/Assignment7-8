from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash

dash.register_page(__name__, path='/')

url = "https://raw.githubusercontent.com/chandanverma07/DataSets/master/Car_sales.csv"
df = pd.read_csv(url)

layout = html.Div([
    html.H2("Car Value Dashboard"),
    dcc.Dropdown(
        id="select-manufacturer",
        options=[{"label": i, "value": i} for i in df['Manufacturer'].unique()],
        value=df['Manufacturer'].unique()[0],
        clearable=False,
    ),
    dcc.Graph(id="sales-bar-chart"),
    dcc.Graph(id="resale-scatter-chart"),
])

@dash.callback(
    Output("sales-bar-chart", "figure"),
    Input("select-manufacturer", "value"))
def update_sales_chart(selected_manufacturer):
    filtered_df = df[df['Manufacturer'] == selected_manufacturer]
    return px.bar(filtered_df, x="Model", y="Sales in thousands", title="Car Sales by Model")

@dash.callback(
    Output("resale-scatter-chart", "figure"),
    Input("select-manufacturer", "value"))
def update_resale_chart(selected_manufacturer):
    filtered_df = df[df['Manufacturer'] == selected_manufacturer]
    return px.scatter(filtered_df, x="Sales in thousands", y="4-year resale value", color="Model",
                      title="Resale Value vs. Sales")