from dash import Input, Output, State, ctx, dcc, html
from dash.exceptions import PreventUpdate

from pytemplates.app import app
from pytemplates.components.whoami_table import WhoamiTable

Form = html.Div(
    className="form-container",
    children=[
        html.Div(
            className="form",
            children=[
                html.H2(
                    className="button-header",
                    children="Enter your name:",
                ),
                html.Div(
                    className="row",
                    children=[
                        html.Button("Greet", id="hello-btn"),
                        dcc.Input(id="hello-user", type="text"),
                    ],
                ),
                html.Div(
                    className="row",
                    children=[
                        html.Button("Wish Farewell", id="goodbye-btn"),
                        dcc.Input(id="goodbye-user", type="text"),
                    ],
                ),
                html.H2(
                    className="button-header",
                    children="Check where the request is handled:",
                ),
                html.Button("Whoami", id="whoami-btn"),
            ],
        ),
    ],
)

Result = html.Div(id="result", className="result-container", children="")


@app.callback(
    inputs=[
        Input("hello-btn", "n_clicks"),
        Input("goodbye-btn", "n_clicks"),
        Input("whoami-btn", "n_clicks"),
    ],
    output=[
        Output("result", "children"),
        Output("hello-user", "value"),
        Output("goodbye-user", "value"),
    ],
    state=[State("hello-user", "value"), State("goodbye-user", "value")],
)
def update_result(
    hello_clicks, goodbye_clicks, whoami_clicks, hello_user, goodbye_user
):
    button_clicked = ctx.triggered_id

    # Do not show any result until a button is pressed
    if hello_clicks is None and goodbye_clicks is None and whoami_clicks is None:
        raise PreventUpdate

    if button_clicked == "whoami-btn":
        return [WhoamiTable, "", ""]
    elif button_clicked == "hello-btn" and hello_user:
        return [f"Hello {hello_user}!", "", ""]
    elif button_clicked == "goodbye-btn" and goodbye_user:
        return [f"Goodbye {goodbye_user}!", "", ""]
    else:
        return ["Please provide a username.", "", ""]
