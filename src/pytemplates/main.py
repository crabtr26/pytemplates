from dash import html

from pytemplates.app import app
from pytemplates.components.body import Body, Header, Result

server = app.server

app.layout = html.Div(className="app", children=[Header, Body, Result])

if __name__ == "__main__":
    app.run_server(debug=True)
