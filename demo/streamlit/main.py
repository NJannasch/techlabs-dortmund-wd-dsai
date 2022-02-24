import csv

import numpy as np
import plotly.figure_factory as ff
import streamlit as st


@st.cache
def read_data(delimiter=","):
    # Read data from csv file
    data = []
    with open("data.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        data = list(reader)
    return data

def create_random_array():
    return list(np.random.rand(25))

# Add some description to page
st.set_page_config(layout="wide")
st.title('Demo to load data from CSV and visualize using streamlit')

def create_plotly_graph(_data, description):
    fig = ff.create_distplot(
            [_data], [description], bin_size=[5]
    )
    return fig

def create_plot(data, key, description):
    # Create graph with plotly, seaborn, matplotlob...
    _data = [float(data[key]) for data in read_data()]
    fig = create_plotly_graph(_data, description)

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

# Create a graph
with st.form("create_graph"):
    st.write("Create graph")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        create_plot(read_data(), 'age', 'Age')

# Using some numpy math stuff
with st.form("get_random_data"):
    st.write("Get random data")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        fig = create_plotly_graph(create_random_array(), 'Random numbers')
        st.plotly_chart(fig, use_container_width=True)

# Create a nice looking table from the raw data
with st.form("get_data"):
    st.write("Get data table")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.table(read_data())
