#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Qtica import Api, Args
from Qtica.core import BehaviorDec
from Qtica.layouts import VLayout
from Qtica.widgets import (
    Application, 
    Container, 
    Label, 
    MainWindow, 
    PushButton, 
    OverlayWidget
)


class Window(BehaviorDec):
	def __init__(self):
		return MainWindow(
			child = OverlayWidget(
				uid = "overlay_widget",
				overlay = Container(
					setFixedSize = Args(300, 100),
					qss = {
						"background-color": "#008080",
						"border-radius": "8px"
					},
					child = VLayout(
						children = [
							Label(
								setText = "This is an overlay widget with a button to hide it"
							),
							PushButton(
								setText = "Hide overlay",
								clicked = lambda: Api.fetch("overlay_widget").overlay_hide()
							)
						]
					)
				),
				child = VLayout(
					children = [
						PushButton(
							setText = f"Button {i}",
							setMinimumHeight = 200,
							clicked = lambda: Api.fetch("overlay_widget").overlay_show()
						)
						for i in range(3)
					]
				)
			)
		)

if __name__ == "__main__":
	app = Application([])
	window = Window()
	window.resize(800, 600)
	window.show()
	app.run(True)