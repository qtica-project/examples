#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Qtica import BehaviorDec, Args
from Qtica.widgets import DockWidget, MainWindow, Application
from PySide6.QtCore import Qt
import sys


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            addDockWidget = [
                Args(
                    Qt.DockWidgetArea.TopDockWidgetArea,
                    DockWidget(
                        setTitle="Dock Widget 1"
                    )
                ),
                Args(
                    Qt.DockWidgetArea.BottomDockWidgetArea,
                    DockWidget(
                        setTitle="Dock Widget 2"
                    )
                )
            ]
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.show()
    app.run()