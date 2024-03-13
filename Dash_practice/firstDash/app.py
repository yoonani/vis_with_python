# origin : https://medium.com/@nuryaumi10/build-interactive-dashboard-using-python-dash-8d145037123

# dash_boostrap_components: to configure our dashboard layout, style, and use some components from dash bootstrap instead of dash default component.
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc, callback, Output, Input

# data from kaggle : https://www.kaggle.com/datasets/desalegngeb/students-exam-scores
df = pd.read_csv("data/data.csv")

avg_math_score = round(df["MathScore"].mean(), 2)
avg_reading_score = round(df["ReadingScore"].mean(), 2)
avg_writing_score = round(df["WritingScore"].mean(), 2)

# initialize app
# bootstrap component 사용을 위해 external_stylesheets에 dbc.themes.BOOTSTRAP 전달
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# create color palette
color_discrete_sequence = ['#0a9396','#94d2bd','#e9d8a6','#ee9b00', '#ca6702', '#bb3e03', '#ae2012']


# create reusable card component
def get_card_component(title, data):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4(title),
                            html.H4(data)
                        ]),
                        color="dark",
                        outline=True,
                        className = 'text-dark',
                        style={'textAlign': 'center', 'margin-bottom': '20px'}
                    ),
                )
    return component

# Define Layout
app.layout = html.Div([
    html.H1(children='Student Exam Scores', style={'textAlign': 'center', 'padding-bottom': '20px'}),
    dbc.Row([
        get_card_component('Total Students', '{:,}'.format(len(df.index))),
        get_card_component('Avg Math Score', str(avg_math_score)),
        get_card_component('Avg Writing Score', str(avg_writing_score)),
        get_card_component('Avg Reading Score', str(avg_reading_score)),

    ]),
    dbc.Row(
        dbc.Col([
            html.H4("Score Distribution"),
            html.Div(
                dbc.RadioItems(
                    id="score-distribution-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=[
                        {'label': 'Math Score', 'value': 'MathScore'},
                        {'label': 'Writing Score', 'value': 'WritingScore'},
                        {'label': 'Reading Score', 'value': 'ReadingScore'},
                    ],
                    value='MathScore',
                ),
                className="radio-group",
                style={'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id="score-distribution-histogram")
        ])
    ),
], style={"margin": "50px 50px 50px 50px"})


# callback
@callback(
    Output("score-distribution-histogram", "figure"),
    Input("score-distribution-radios", "value")
)
def update_histogram(value):
    figure=px.histogram(df, x=value, color_discrete_sequence=['#0a9396'])
    return figure


if __name__ == '__main__':
    app.run(debug=True)