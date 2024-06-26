#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from Qtica import BehaviorDec, Property
from Qtica.tools import EasingCurve, Palette, Color
from Qtica.widgets import Container, MainWindow, Application, PushButton
from Qtica.animations import SequentialAnimationGroup, ParallelAnimationGroup, PropertyAnimation
from PySide6.QtCore import QRect
from _utils import get_random_color


def get_animations(index: int):
    return [
        PropertyAnimation(
            setPropertyName = b'geometry',
            setStartValue = QRect(50, index * 50, 100, 100),
            setEndValue = QRect(400, index * 50, 100, 100),
            setDuration = 1000 * 2,
            setEasingCurve = EasingCurve.InOutQuad
        ),
        PropertyAnimation(
            setPropertyName = b'minimumWidth',
            setStartValue = 50,
            setEndValue = 200,
            setDuration = 1000 * 2,
            setEasingCurve = EasingCurve.InOutQuad
        ),
        PropertyAnimation(
            setPropertyName = b'color',
            setStartValue = get_random_color(),
            setEndValue = get_random_color(),
            setDuration = 1000 * 2,
            setEasingCurve = EasingCurve.InOutQuad
        )
    ]


class Button(PushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_color(self):
        return self.palette().color(Palette.ColorRole.Button)

    def set_color(self, color):
        palette = self.palette()
        palette.setColor(Palette.ColorRole.Button, color)
        self.setPalette(palette)

    color = Property(Color, get_color, set_color)


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            child = Container(
                child = [
                    Button(
                        setText = "PropertyAnimation",
                        animations = get_animations(1)
                    ),
                    Button(
                        setText = "ParallelAnimationGroup",
                        animations = [
                            ParallelAnimationGroup(
                                running = True,
                                addAnimation = get_animations(5)
                            )
                        ]
                    ),
                    Button(
                        setText = "SequentialAnimationGroup",
                        animations = [
                            SequentialAnimationGroup(
                                running = True,
                                addAnimation = get_animations(9)
                            )
                        ]
                    )
                ]
            )
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.resize(800, 600)
    window.show()
    app.run()