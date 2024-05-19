from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFont
from WorkWidget.Widget_Components import Label, LineEdit, Button


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, main_widget):
        super().__init__(main_widget)
        self.grid_layout = QtWidgets.QGridLayout()

        title_label = Label(self, 'Show Student', font_size=18)
        self.grid_layout.addWidget(title_label)

        self.setLayout(self.grid_layout)
