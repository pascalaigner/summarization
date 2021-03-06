import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

def tab_wordcloud_tfidf():
    vertical_space = "15px"
    tab = dbc.Tab(label="Visualization TF-IDF", children=[
        html.Div(style={"height": vertical_space}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            children=[
                                html.Span("This tab provides an animation of TF-IDF."),
                                html.Span(" With the parameter "),
                                html.I("Textblock length"),
                                html.Span(" the block length in minutes can be adjusted."),
                                html.Span(" The x-axis shows the term frequency of the word in the current textblock"),
                                html.Span(" and the y-axis the inverse document frequency."),
                                html.Span(" Note that 1/3 means the word occurs in 1 of 3 textblocks etc."),
                                html.Span(" The case where a word occurs in all of the textblocks is not shown."),
                                html.Span(" For a detailed description of TF-IDF we refer to our paper."),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(style={"height": vertical_space}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Parameters"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div("Textblock length"),
                                        html.Div("in minutes"),
                                    ],
                                    width="auto",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Input(
                                            id="textblock_length_input3",
                                            type="number",
                                            min=1,
                                            max=100,
                                            step=1,
                                            value=5,
                                        ),
                                    ],
                                    width="auto",
                                ),
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.Div(style={"height": "27px"}),
                        dbc.Button(
                            "Apply",
                            id="apply_wordcloud_settings3",
                            className="btn-outline-primary",
                        ),
                    ],
                    width="auto",
                ),

            ],
        ),
        html.Div(style={"height": vertical_space}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Loading(
                            id="loading_wctfidf",
                            color="#1a1a1a",
                            children=[
                                dcc.Graph(
                                    id="animation_tfidf",
                                    figure={'layout': go.Layout(margin={'t': 0, "b":0, "r":0, "l":0})},
                                    config={"displayModeBar": False},
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
    )
    return tab