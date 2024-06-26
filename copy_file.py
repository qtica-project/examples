#!/usr/bin/python3

from Qtica.core import (
    BehaviorDec,
    AbstractWidget,
    Api
)

from Qtica.widgets import (
    App,
    MainWindow,
)

from Qtica.layouts import (
    FormLayout,
    VLayout,
    HLayout
)

from Qtica.tools import (
    CopyProgress,
    FormLayoutWrapper
)

from PySide6.QtWidgets import (
    QPushButton,
    QProgressBar,
    QLineEdit,
    QLabel
)

def push_button(text: str, on_click):
    btn = QPushButton()
    btn.setText(text)
    btn.clicked.connect(on_click)
    return btn


class LineEdit(AbstractWidget, QLineEdit):
    def __init__(self, *args, **kwargs):
        QLineEdit.__init__(self)
        super().__init__(**kwargs)


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            uid = "window",
            windowTitle="Copy Progress Example",
            child=VLayout(
                children=[
                    FormLayout(
                        children=[
                            FormLayoutWrapper(
                                label=QLabel("Enter Source file"),
                                field=LineEdit(
                                    uid="src", 
                                    signals=[
                                            ("textChanged", 
                                             lambda value: Api.fetch("cp").set_src(value))
                                        ]
                                    ),
                            ),
                            FormLayoutWrapper(
                                label=QLabel("Enter Destintioin path"),
                                field=LineEdit(
                                    uid="dst", 
                                    signals=[
                                        ("textChanged", 
                                         lambda value: Api.fetch("cp").set_dst(value))
                                    ]
                                ),
                            )
                        ]
                    ),

                    CopyProgress(
                        uid = "cp",
                        child=QProgressBar(maximum=100),
                        src=Api.fetch("src").text(),
                        dst=Api.fetch("dst").text(),
                        overwrite=True,
                        signals = [
                            ("copy_progress", lambda value: print(f"{value}%")),
                            ("copy_done", lambda: print("Copy Done"))
                        ]
                    ),

                    HLayout(
                        children=[
                            push_button("Copy", Api.declarative_fetch("cp").start),
                            push_button("Pause", Api.declarative_fetch("cp").pause),
                            push_button("Resum", Api.declarative_fetch("cp").resum)
                        ]
                    )
                ]
            )
        )


def main():
    import sys
    app = App(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()