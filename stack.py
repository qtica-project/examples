#!/usr/bin/python3

from Qtica import BehaviorDec
from Qtica.layouts import StackedLayout
from Qtica.widgets import App, MainWindow, Label
from PySide6.QtCore import QSize


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            home=StackedLayout(
                setStackingMode = StackedLayout.StackingMode.StackAll,
                children=[
                    Label(
                        setFixedSize=QSize(size, size),
                        qss={
                            "background-color": color
                        }
                    )
                    for color, size in 
                    zip(("red", "green", "blue"), (200, 170, 150))
                ]
            )
        )

if __name__ == "__main__":
    import sys

    app = App(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())