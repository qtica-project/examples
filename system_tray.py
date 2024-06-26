#!/usr/bin/python3

import os
import sys
from Qtica.widgets import Application, Menu
from Qtica.tools import (
    SystemTray,
    Action,
    MenuSeparatorWrapper,
    MenuAction,
    Icon
)

def get_user_name() -> str:
    return os.environ.get("USER").title()

app = Application(sys.argv)
sys_tray = SystemTray(
    setIcon=Icon("assets/logo.png"),
    setToolTip="Test Qtica Tray",
    setContextMenu=Menu(
        children=[
            Action(
                setIcon=Icon.fromTheme("browser"),
                setText="Web Browser",
                triggered=lambda: print("Hi, I'm Browser!")
            ),
            Action(
                setIcon=Icon("assets/logo.png"),
                setText="Qtica Tool Kit",
                triggered=lambda: print("Hi, I'm Qtica!")
            ),
            MenuSeparatorWrapper(),
            MenuAction(
                text="What's My name?!",
                icon=Icon.fromTheme("user"),
                callback=lambda: print(f"Your name is '{get_user_name()}'")
            ),
            MenuAction(
                text="Quit",
                icon=Icon.fromTheme("exit"),
                callback=Application.exit
            )
        ]
    )
)

sys_tray.show()
app.run(True)