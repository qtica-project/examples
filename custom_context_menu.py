#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from Qtica import BehaviorDec, Qt
from Qtica.tools import Cursor, MenuAction
from Qtica.widgets import MainWindow, Application, Frame, Menu
from _utils import get_random_color


def context_menu():
    Menu(
        children=[
            MenuAction(
                text="Python"
            ),

            MenuAction(
                text="JavaScript"
            ),
            MenuAction(
                text="C++"
            )
        ]
    ).exec(Cursor.pos())


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            child = Frame(
                qss = {
                    "background-color": get_random_color().name(),
                    "border-radius": "8px",
                    "margin": "10px"
                },
                signals={
                    "customContextMenuRequested": context_menu
                },
                setContextMenuPolicy=Qt.ContextMenuPolicy.CustomContextMenu
            )
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.resize(800, 600)
    window.show()
    app.run()
