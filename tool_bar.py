#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from Qtica import BehaviorDec, Args
from Qtica.widgets import ToolBar, MainWindow, Application
import sys



class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            addToolBar = [
                Args(
                    Qt.ToolBarArea.TopToolBarArea,
                    ToolBar()
                ),
                Args(
                    Qt.ToolBarArea.BottomToolBarArea,
                    ToolBar()
                )
            ]
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.show()
    app.run()