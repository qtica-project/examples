# import qtica_path

from PySide6.QtCore import Qt
from Qtica import (
    BehaviorDec,
    Api
)

from Qtica.widgets import (
    Application,
    MainWindow,
    PushButton
)

from Qtica.layouts import (
    VLayout
)

from Qtica.tools import Color, Brush
from Qtica.painters  import StatusEdgePaint


class Home(BehaviorDec):
    def update_status(self):
        btn = Api.fetch("status_btn")
        paint = Api.fetch("status_paint")

        if btn.text().startswith("On"):
            self._brush.setColor(Qt.GlobalColor.red)
            paint.set_brush(self._brush)
            btn.setText("Offline")
            return

        self._brush.setColor(Qt.GlobalColor.green)
        paint.set_brush(self._brush)
        btn.setText("Online")

    def __init__(self):
        self._brush = Brush(setColor=Color("green"), setStyle=Qt.BrushStyle.SolidPattern)

        return VLayout(
            children=[
                PushButton(
                    text="Change Status",
                    signals=[
                        ("clicked", lambda: self.update_status())
                    ]
                ),
                StatusEdgePaint(
                    uid="status_paint",
                    brush=self._brush,
                    child=PushButton(
                        uid="status_btn",
                        text="Online"
                    )
                )
            ]
        )


class Window(BehaviorDec):
    def __init__(self) -> None:
        return MainWindow(
            uid="window",
            home=Home()
        )


def main():
    import sys

    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()