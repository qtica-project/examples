#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from Qtica import BehaviorDec, Args, MArgs, Qt
from Qtica.layouts import VLayout
from Qtica.widgets import Container, Label, MainWindow, Application, ScrollArea
from Qtica.tools import ConicalGradient, LinearGradient, RadialGradient, SizePolicy
from Qtica.effects import DropShadowEffect


def label(text: str) -> Label:
    return Label(
        setText = text,
        qss = {
            "font-size": "16px",
            "text-shadow": "3px 3px 10px red"
        },
        setSizePolicy = SizePolicy(SizePolicy.Policy.Preferred, 
                                   SizePolicy.Policy.Fixed)
    )

def widget(qss: dict[str, str]) -> Container:
    qss.setdefault("border-radius", "10px")
    return Container(
        setMinimumHeight = 150,
        qss = qss
    )


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            child = ScrollArea(
                child = VLayout(
                    children = [
                        label("Conical Gradient"),
                        widget({
                            "background": ConicalGradient(
                                setCenter = Args(0.5, 0.5),
                                setAngle = 0,
                                setColorAt = MArgs(
                                    Args(0.0, Qt.GlobalColor.red),
                                    Args(0.25, Qt.GlobalColor.yellow),
                                    Args(0.5, Qt.GlobalColor.green),
                                    Args(0.75, Qt.GlobalColor.blue),
                                    Args(1.0, Qt.GlobalColor.red)
                                    )
                                )
                            }
                        ),
                        label("Radial Gradient"),
                        widget({
                            "background": RadialGradient(
                                setCenter = Args(0.5, 0.5), 
                                setFocalPoint = Args(0.7, 0.7),
                                setColorAt = MArgs(
                                    Args(0.0, Qt.GlobalColor.red),
                                    Args(0.25, Qt.GlobalColor.yellow),
                                    Args(0.5, Qt.GlobalColor.green),
                                    Args(0.75, Qt.GlobalColor.blue),
                                    Args(1.0, Qt.GlobalColor.red)
                                    )
                                )
                            }
                        ),
                        label("Linear Gradient"),
                        widget({
                            "background": LinearGradient(
                                setStart = Args(0, 0),
                                setFinalStop = Args(0, 1),
                                setColorAt = MArgs(
                                    Args(0.0, Qt.GlobalColor.red),
                                    Args(0.25, Qt.GlobalColor.yellow),
                                    Args(0.5, Qt.GlobalColor.green),
                                    Args(0.75, Qt.GlobalColor.blue),
                                    Args(1.0, Qt.GlobalColor.red)
                                    )
                                )
                            }
                        ),
                        label("Custom Border Radius"),
                        widget({
                            "background": "#008080",
                            "border-radius": "30px 1px 30px 1px"
                        }),
                        label("Custom Box Shadow"),
                        widget({
                            "background": "#008080",

                            ## using CSS box-shadow directly
                            # "box-shadow": "5px 5px 15px lightblue",
                            "box-shadow": "0 6px 20px 0 rgba(0, 0, 0, 0.19)",

                            ## using QtWidgets.QGraphicsDropShadowEffect object
                            ## NOTE: you can use BoxShadow!
                            # "box-shadow": DropShadowEffect(
                            #     setOffset = Args(5, 5),
                            #     setBlurRadius = 15,
                            #     setColor = "lightblue"
                            # )
                            })
                    ]
                )
            )
        )


if __name__ == "__main__":
    app = Application(sys.argv)
    window = Window()
    window.resize(600, 600)
    window.show()
    app.run()
