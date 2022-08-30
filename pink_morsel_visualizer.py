import pandas as pd 
from dash import Dash, html, dcc, Input, Output
from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./formatted_data.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)


# create the visualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)