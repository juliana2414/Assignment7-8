from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash

dash.register_page(__name__, path='/page2')

df = pd.read_csv("https://raw.githubusercontent.com/chandanverma07/DataSets/master/Car_sales.csv")

layout = html.Div([
    html.H2("Additional Insights"),
    dcc.Dropdown(
        id='yaxis-column',  
        options=[{'label': i, 'value': i} for i in df.columns if i not in ['Model', 'Manufacturer']],
        value='Sales in thousands',
        clearable=False
    ),
    dcc.Graph(id='manufacturer-distribution-graph')
])


@dash.callback(
    Output('manufacturer-distribution-graph', 'figure'),
    Input('yaxis-column', 'value')
)
def update_graph(yaxis_column_name):
    sorted_df = df.sort_values(by=yaxis_column_name, ascending=True)
    return px.scatter(df, x="Manufacturer", y=yaxis_column_name, title=f"Manufacturer Insights vs {yaxis_column_name}")
