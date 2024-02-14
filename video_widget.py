#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from Qtica import BehaviorDec, Args
from Qtica.tools import MediaPlayer
from Qtica.widgets import MainWindow, VideoWidget, Application
from PySide6.QtMultimedia import QAudioDevice, QAudioOutput
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QDir


class Window(BehaviorDec):
    def _get_video_file(self) -> str:
        video_file,_  = QFileDialog().getOpenFileName(caption="Select a Video", 
                                                      dir=QDir.homePath(), 
                                                      filter="Video (*.mov *.mp4 *.m4a *.3gp *.3g2 *.mj2)")
        if not video_file:
            sys.exit(127)

        print("video path: ", video_file)
        return video_file

    def __init__(self):
        return MainWindow(
            methods=[("resize", Args(800, 600))],
            home=VideoWidget(
                setFixedSize=Args(400, 400),
                player=MediaPlayer(
                    setLoops = -1,
                    setSource = self._get_video_file(),
                    setAudioOutput = QAudioOutput(QAudioDevice()),
                    running=True
                )
            )
        )

def main():
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()