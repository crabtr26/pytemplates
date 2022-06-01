from dash import html

from pytemplates.app import app
from pytemplates.components.body import Form, Result
from pytemplates.components.header import Header

server = app.server

app.layout = html.Div(className="app", children=[Header, Form, Result])

if __name__ == "__main__":
    app.run_server(debug=True)
