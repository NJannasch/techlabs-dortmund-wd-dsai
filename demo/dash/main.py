import csv

import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from businesslogic import create_random_array
from dash import Dash, Input, Output, dash_table, dcc, html

app = Dash(__name__)


def read_data(delimiter=","):
    # Read data from csv file
    data = []
    with open("data.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        data = list(reader)
    return data


def create_plotly_graph(_data, description):
    # Helper function to create graph
    fig = ff.create_distplot(
            [_data], [description], bin_size=[len(_data)/25]
    )
    return fig


app.layout = html.Div(children=[
    html.H1(children='Demo to load data from CSV and visualize using dash'),
    # Define dummy input
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text'),
    ]),
    # Define dummy output
    html.Div(id='my-output'),
    ################################################################
    # Graphs
    html.Div([
        "Filter:",
        dcc.Dropdown(
                id='filterby',
                options = list(read_data()[0].keys()),
                value='age'
            ),
            dcc.Graph(
                id='example-graph',
                figure=create_plotly_graph(
                    [float(data['age']) for data in read_data()],
                    'Ages'
            )
    )
    ]),
    dcc.Graph(
        id='example-graph2',
        figure=create_plotly_graph(
            create_random_array(),
            'Random numbers'
            )
    ),
    dash_table.DataTable(read_data())
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='filterby', component_property='value')
)
def update_graph(input_value):
    return create_plotly_graph([float(data[input_value]) for data in read_data()], input_value)
    


if __name__ == '__main__':
    app.run_server(debug=True)
