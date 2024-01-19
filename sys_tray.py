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
    setIcon=Icon.fromTheme("qt"),
    setToolTip="Test Qtica Tray",
    setContextMenu=Menu(
        children=[
            Action(
                setIcon=Icon.fromTheme("firefox"),
                setText="Firefox",
                triggered=lambda: print("Hi, I'm Firefox")
            ),
            Action(
                setIcon=Icon.fromTheme("python"),
                setText="Python",
                triggered=lambda: print("Hi, I'm Python")
            ),
            MenuSeparatorWrapper(),
            MenuAction(
                text="What's My name!?",
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
app.run()