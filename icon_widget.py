#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from Qtica import Args, BehaviorDec, Api, Qt
from Qtica.enums import Colors
from Qtica.layouts import VLayout
from Qtica.tools import Icon, Movie
from Qtica.widgets import Application, IconWidget, MainWindow, ScrollArea, Slider


class IconWidgetDemo(BehaviorDec):
    def movie_player(self):
        movie: Movie = Api.fetch("movie")
        movie_slider: Slider = Api.fetch("movie_slider")

        movie_slider.setValue(movie.currentFrameNumber())

        if movie.is_paused:
            movie.resum()
            movie_slider.setHidden(True)
        else:
            movie.pause()
            movie_slider.setHidden(False)

    def __init__(self):
        return MainWindow(
            child = ScrollArea(
                setSizeAdjustPolicy = ScrollArea.SizeAdjustPolicy.AdjustToContents,
                child = VLayout(
                    children=[
                        IconWidget(
                            icon = Movie(
                                uid = "movie",
                                file = "assets/notify.webp"
                            ),
                            setMinimumSize = Args(256, 512),
                            events = {
                                "mousePress": lambda e: self.movie_player()
                            }
                        ),
                        Slider(
                            uid = "movie_slider",
                            setHidden = True,
                            setOrientation = Qt.Orientation.Horizontal,
                            setMinimum = 0,
                            setPageStep = 1,
                            setMaximum = Api.fetch("movie").frameCount() - 1,
                            signals = {
                                "valueChanged": Api.fetch("movie").jumpToFrame
                            }
                        ),
                        IconWidget(
                            icon = Icon.fromTheme("network-wireless"),
                            setMinimumSize = Args(256, 512)
                        ),
                        IconWidget(
                            icon = Icon("assets/notify.svg"),
                            setMinimumSize = Args(256, 512),
                            color = Colors.orange
                        ),
                        IconWidget(
                            icon = Icon("assets/notify.png"),
                            setMinimumSize = Args(256, 512)
                        )
                    ]
                )
            )
        )

if __name__ == "__main__":
    app = Application(sys.argv)
    window = IconWidgetDemo()
    window.show()
    app.run()