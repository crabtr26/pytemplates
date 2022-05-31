import json
import os
import socket

from dash import Input, Output, State, ctx, dcc, html
from dash.exceptions import PreventUpdate

from pytemplates.app import app

Body = html.Div(
    className="form-container",
    children=[
        html.Div(
            className="form",
            children=[
                html.H2(
                    className="button-header",
                    children="Enter your name to recieve a greeting",
                ),
                html.Button("Greet", id="hello-submit"),
                dcc.Input(id="hello-input", type="text"),
                html.H2(
                    className="button-header",
                    children="Enter your name to recieve a wish farewell",
                ),
                html.Button("Wish Farewell", id="goodbye-submit"),
                dcc.Input(id="goodbye-input", type="text"),
                html.H2(
                    className="button-header",
                    children="Check where the request is handled",
                ),
                html.Button("Whoami", id="whoami-submit"),
            ],
        )
    ],
)

Result = html.Div(id="output", className="output-container", children="")

Header = html.H1(className="app-header", children="PyTemplates")


@app.callback(
    Output("output", "children"),
    inputs=[
        Input("hello-submit", "n_clicks"),
        Input("goodbye-submit", "n_clicks"),
        Input("whoami-submit", "n_clicks"),
    ],
    state=[State("hello-input", "value"), State("goodbye-input", "value")],
)
def update_output(
    hello_clicks, goodbye_clicks, whoami_clicks, hello_user, goodbye_user
):
    button_clicked = ctx.triggered_id

    if hello_clicks is None and goodbye_clicks is None and whoami_clicks is None:
        raise PreventUpdate

    if button_clicked == "whoami-submit":
        table = html.Table(
            id="whoami-table",
            children=[
                html.Tr(
                    children=[
                        html.Th("Host Name"),
                        html.Th("Host IP"),
                        html.Th("Process ID"),
                    ]
                ),
                html.Tr(
                    children=[
                        html.Th(socket.gethostname()),
                        html.Th(socket.gethostbyname(socket.gethostname())),
                        html.Th(os.getpid()),
                    ]
                ),
            ],
        )
        return table
    elif button_clicked == "hello-submit" and hello_user:
        return f"Hello {hello_user}!"
    elif button_clicked == "goodbye-submit" and goodbye_user:
        return f"Goodbye {goodbye_user}!"
    else:
        return "Please provide a username."
