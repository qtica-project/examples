#!/usr/bin/python3

import os
import sys
from PySide6.QtGui import QColor
from PySide6.QtCore import QSize, Qt
from Qtica.widgets import FramelessWindow, Label, Application, Container, ToolButton
from Qtica.services import randomColor, colorToHex
from Qtica.layouts import HLayout
from Qtica.widgets.dialogs.mask import QSpacerItem, SizePolicy
from Qtica.widgets.icon_widget import Icon
from Qtica import BehaviorDec, Api


class Window(BehaviorDec):
    def get_text_color(self, color: QColor) -> QColor:
        luma = ((0.299 * color.red()) + (0.587 * color.green()) + (0.114 * color.blue())) / 255
        return QColor(0, 0, 0) if luma > 0.5 else QColor(255, 255, 255)

    def update_background(self):
        bg_color = randomColor()
        fg_color = self.get_text_color(bg_color)

        Api.fetch("window").qss.update({"background-color": bg_color.name()})
        Api.fetch("label").qss.update({"color": fg_color.name()})

    def __init__(self):
        return FramelessWindow(
            uid="window",
            windowTitle="Welcome Qtica!",
            title_bar=Container(
                child=HLayout(
                    children=[
                        QSpacerItem(0, 0, SizePolicy.Policy.Expanding, SizePolicy.Policy.Fixed),
                        ToolButton(
                            setIcon=Icon.fromTheme("window-close"),
                            setFixedSize=QSize(32, 32),
                            signals=[("clicked", lambda: Api.fetch("window").close())],
                            qss={
                                "border": "none",
                                "background": "none"
                            }
                        )
                    ]
                ),
                qss={
                    "background-color": "#eee",
                }
            ),
            methods = [
                ("resize", QSize(400, 200))
            ],
            home=Label(
                uid="label",
                setText=f"Hello {os.environ.get('USER', '')}, Welcome to Qtica.<br>Click me!",
                setTextFormat=Qt.TextFormat.RichText,
                setAlignment=Qt.AlignmentFlag.AlignCenter,
                events = [("mousePress", lambda _: self.update_background())],
                qss={"font-size": "24px"}
            ),
            qss={"background-color": colorToHex(randomColor())},
        )

app = Application(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())