# callback use
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input


#  Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(children="My first app with data, graph and controls"),
        html.Hr(),
        dcc.RadioItems(
            options=["pop", "lifeExp", "gdpPercap"],
            value="lifeExp",
            id="controls-and-radio-item",
        ),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        dcc.Graph(figure={}, id="controls-and-graph"),
    ]
)


@app.callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


if __name__ == "__main__":
    app.run()
