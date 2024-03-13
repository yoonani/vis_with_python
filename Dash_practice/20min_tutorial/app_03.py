# working with plotly

import pandas as pd

# dcc : dash core component
from dash import Dash, html, dash_table, dcc
import plotly.express as px

#  Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(children="My first app with data and graph"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg")),
    ]
)

if __name__ == "__main__":
    app.run()
