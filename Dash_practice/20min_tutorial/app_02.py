# working with data

import pandas as pd
from dash import Dash, html, dash_table

#  Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(children="My first app with data"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    ]
)

if __name__ == "__main__":
    app.run()
