import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

def tab_wordcloud_draft():
    vertical_space = "15px"

    tab = dbc.Tab(label="Wordcloud draft", children=[
        html.Div(style={"height": vertical_space}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            children=[
                                html.Span("This tab provides a visual overview over the most frequent words in each text block."),
                                html.Span(" With the parameter "),
                                html.I("Textblock length"),
                                html.Span(" the block length in minutes can be adjusted."),
                                html.Span(" With the slider the individual blocks can be selected."),
                                html.Span(" The Wordcloud is based on word frequency."),
                                html.Span(" The bigger a word is written, the more occurrences it has in the selected textblock."),
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
                                            id="textblock_length_input",
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
                            id="apply_wordcloud_settings",
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
                            id="loading_wcdraft",
                            color="#1a1a1a",
                            children=[
                                dcc.Graph(
                                    id="wordcloud_plot",
                                    figure={'layout': go.Layout(margin={'t': 0, "b":0, "r":0, "l":0})},
                                    #config={"displayModeBar": False},
                                    #style={"height": "600px"},
                                ),
                            ],
                        ),
                    ],
                ),
                dbc.Col(
                    [   
                        html.Div(
                            id = "vertical_slider",
                            style = {"visibility": "hidden"},
                            children = [
                                dcc.Slider(
                                    id="wordcloud_steps_slider",
                                    min=0,
                                    max=9,
                                    step = 1,
                                    value = 9,
                                    marks={},
                                    vertical = True,        
                                ),
                            ],
                        ),  
                    ], width=1,
                ),
            ],
        ),
    ],
    )
    return tab