#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from Qtica import BehaviorDec, Args, Qt
from Qtica.layouts import VLayout
from Qtica.tools import SizePolicy, Color
from Qtica.widgets import (
    Container,
    IconWidget, 
    Label, 
    MainWindow, 
    Application, 
    ScrollArea
)
from Qtica.effects import (
    BoxShadow, 
    ShadowEffect,
    ColorizeEffect,
    OpacityEffect,
    BlurEffect,
    DropShadowEffect,
)


def label(text: str, **kwargs) -> Label:
    return Label(
        setText = text,
        qss = {
            "font-size": "16px"
        },
        setSizePolicy = SizePolicy(SizePolicy.Policy.Preferred, 
                                   SizePolicy.Policy.Fixed),
        **kwargs
    )

def widget(effect) -> Container:
    qss = {
        "border-radius": "10px",
        # "background-color": "#1D2A35"
    }

    return IconWidget(
        setMinimumHeight = 150,
        setGraphicsEffect = effect,
        qss = qss,
        icon = "assets/logo-name.png"
    )


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            child = ScrollArea(
                child = Container(
                    qss = {"background-color": "#008080"},
                    child = VLayout(
                    children = [
                        label("Box Shadow Effect"),
                        widget(
                            BoxShadow(
                                children = [
                                    ShadowEffect(
                                        setOffset = Args(0, 4),
                                        setBlurRadius = 8,
                                        setColor = "green"
                                        # setColor = Color.fromRgb(0, 0, 0, 0.2 * 255)
                                    ),
                                    ShadowEffect(
                                        setOffset = Args(0, 6),
                                        setBlurRadius = 20,
                                        setColor = "red"
                                        # setColor = Color.fromRgb(0, 0, 0, 0.1 * 255)
                                    )
                                ]
                            )
                        ),
                        label("Colorize Effect"),
                        widget(
                            ColorizeEffect(
                                setStrength = 0.4,
                                setColor = Color("blue")
                            )
                        ),
                        label("Opacity Effect"),
                        widget(
                            OpacityEffect(
                                setOpacityMask = Qt.GlobalColor.cyan,
                                setOpacity = 0.4
                            )
                        ),
                        label("Blur Effect"),
                        widget(
                            BlurEffect(
                                setBlurRadius = 0.4
                            )
                        ),
                        label("Drop Shadow Effect"),
                        widget(
                            DropShadowEffect(
                                setBlurRadius = 15,
                                setOffset = Args(5, 5),
                                setColor = Color("green")
                            )
                        )
                    ]
                )
            )
            )
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.resize(600, 600)
    window.show()
    app.run()