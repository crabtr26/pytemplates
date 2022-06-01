import os
import socket

from dash import html

WhoamiTable = html.Table(
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
