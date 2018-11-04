
import dash
import dash_core_components as dcc
import dash_html_components as html
from calls import app
from calls.routes import *


app.layout = html.Div([

    html.H1('Analyzing NYC 311 Call Data'),

    html.H2('Calls by Zipcode'),
    dcc.Dropdown(
        id='location-dropdown',
        options= locations(),
        multi=True
    ),
    dcc.Graph(
        id='location-histogram',
        figure=complaint_histogram()
        ),


    html.H2('Percentage Calls per Borough'),
    dcc.Graph(
        id="count-histogram",
        figure=borough_count_histogram()
        ),

    html.H2('Call Types per Borough'),
    dcc.Graph(
        id="borough-histogram",
        figure=borough_complaints()
        )
    ])



@app.callback(
    dash.dependencies.Output('location-histogram','figure'),
    [dash.dependencies.Input('location-dropdown','value')])


def update_histogram(location_values):
    hist=complaint_histogram(location_values= location_values)
    return hist

# @app.callback(
#     dash.dependencies.Output('borough-histogram','figure'),
#     [dash.dependencies.Input('borough-dropdown','value')])
#
#
# def update_borough_histogram(location_borough):
#     histb= borough_histogram(location_borough=location_borough)
#     return histb
