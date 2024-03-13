# origin : https://dash.plotly.com/tutorial
# Dash elementary - initial, layout

from dash import Dash, html
import dash_bootstrap_components as dbc

# app initial
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# layout
app.layout = html.Div([html.Div(children="Hello Dash!")])

if __name__ == "__main__":
    app.run(debug=True)
