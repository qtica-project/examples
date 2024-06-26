#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random

from Qtica import Api, BehaviorDec, Qt, PosEvents, PosEventsArg, PosEventsRange
from Qtica.tools import Painter
from Qtica.widgets import MainWindow, Application, Frame
from PySide6.QtGui import QPaintEvent
from _utils import get_random_color


RANDOM_POS = [random.choice(range(50, 700)), random.choice(range(50, 500))]


class PosEventsWidget(Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        qp = Painter(self)
        qp.setRenderHint(qp.RenderHint.Antialiasing | qp.RenderHint.TextAntialiasing)
        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(get_random_color())
        qp.drawRoundedRect(RANDOM_POS[0], RANDOM_POS[1], 30, 30, 8, 8)
        return super().paintEvent(arg__1)


class Window(BehaviorDec):
    def yes_in_pos(self):
        print("yes in pos")
        Api.fetch("pos_widget").update()

    def __init__(self):
        return MainWindow(
            uid = "window",
            child = PosEventsWidget(
                uid = "pos_widget",
                qss = {
                    "background-color": get_random_color().name(),
                    "border-radius": "8px",
                    "margin": "10px"
                },
                at_pos = PosEvents(
                    clicked = [
                        PosEventsArg(
                            x = PosEventsRange(RANDOM_POS[0] - 1, RANDOM_POS[0] + 30),
                            y = PosEventsRange(RANDOM_POS[1] - 1, RANDOM_POS[1] + 30),
                            func = self.yes_in_pos,
                            button = Qt.MouseButton.LeftButton,
                            modifiers = Qt.KeyboardModifier.AltModifier | Qt.KeyboardModifier.ControlModifier
                        )
                    ]
                )
            )
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.resize(800, 600)
    window.show()
    app.run()