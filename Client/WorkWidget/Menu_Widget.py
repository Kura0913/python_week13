from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFont
from WorkWidget.Widget_Components import Label, LineEdit, Button


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_function):
        super().__init__()
        self.update_function = update_function
        self.setObjectName('Menu_Widget')
        box_layout = QtWidgets.QVBoxLayout()
        Add_Button = Button(self, 'Add Student', font_size=14, fix_size=(125, 30))
        Show_Button = Button(self, 'Show all', font_size=14, fix_size=(125, 30))

        box_layout.addWidget(Add_Button, 1)
        box_layout.addWidget(Show_Button, 1)
        box_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        Add_Button.clicked.connect(lambda: self.update_function('add'))
        Show_Button.clicked.connect(lambda: self.update_function('show'))

        self.setLayout(box_layout)
