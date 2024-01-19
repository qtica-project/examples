#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Qtica
from Qtica import BehaviorDec
from Qtica.layouts import VLayout, FormLayout
from Qtica.tools.wrappers import FormLayoutWrapper
from Qtica.widgets import (
    GroupBox,
    MainWindow,
    Application,
    Label,
    DateEdit,
    TimeEdit,
    TextEdit,
    LineEdit
)


class Window(BehaviorDec):
    def __init__(self):
        return MainWindow(
            home=GroupBox(
                setTitle="Appointment Details",
                setFlat=True,
                child=VLayout(
                    children=[
                        FormLayout(
                            children=[
                                FormLayoutWrapper(
                                    label=Label(setText="Date:"),
                                    field=DateEdit()
                                ),
                                FormLayoutWrapper(
                                    label=Label(setText="Time:"),
                                    field=TimeEdit()
                                ),
                                FormLayoutWrapper(
                                    label=Label(setText="Location:"),
                                    field=LineEdit(setText="Meeting room 1")
                                )
                            ]
                        ),
                        TextEdit(
                            setText="""
                            <strong>Developer meeting</strong>
                            <p>
                            A brief meeting to check the status
                            of each project in the development
                            department.
                            </p>
                            """
                        )
                    ]
                )
            )
        )

if __name__ == "__main__":
    import sys

    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())



## PySide6
# from PySide6.QtWidgets import (
#     QMainWindow, 
#     QApplication, 
#     QGroupBox, 
#     QVBoxLayout, 
#     QFormLayout, 
#     QDateEdit, 
#     QTimeEdit, 
#     QLabel,
#     QTextEdit,
#     QLineEdit
# )

# class Window(QMainWindow):
#     def __init__(self, parent: object = None):
#         super().__init__(parent)

#         self.group_box = QGroupBox(self)
#         # self.group_box.setFlat(True)
#         self.group_box.setTitle("Appointment Details")

#         self.label1 = QLabel("Date:")
#         self.label2 = QLabel("Time:")
#         self.label3 = QLabel("Location:")

#         self.date = QDateEdit()
#         self.time = QTimeEdit()
#         self.line = QLineEdit()
#         self.text = QTextEdit()

#         self.text.setText("Developer meeting")

#         self.v_layout = QVBoxLayout()
#         self.f_layout = QFormLayout()

#         self.f_layout.addRow(self.label1, self.date)
#         self.f_layout.addRow(self.label2, self.time)
#         self.f_layout.addRow(self.label3, self.line)

#         self.v_layout.addLayout(self.f_layout)
#         self.v_layout.addWidget(self.text)

#         self.group_box.setLayout(self.v_layout)
#         self.setCentralWidget(self.group_box)

# if __name__ == "__main__":
#     import sys
    
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())
