from PyQt6 import QtWidgets
from WorkWidget.AddStu_Widget import AddStuWidget
from WorkWidget.ShowStu_Widget import ShowStuWidget
from WorkWidget.Menu_Widget import MenuWidget
from WorkWidget.Widget_Components import Label
from Client_Socket import SocketClient


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.client = SocketClient('127.0.0.1', 20001)

        # ----- Set Window Title -----
        self.setObjectName("main_widget")

        # ----- Grid Layout -----
        self.Grid_Layout = QtWidgets.QGridLayout()

        # ----- Title -----
        label = Label(self, "Student Management System", font_size=18)
        self.Grid_Layout.addWidget(label, 0, 0, 1, 2)

        # ----- Function -----
        self.function_widget = FunctionWidget()
        self.Grid_Layout.addWidget(self.function_widget, 1, 1, 1, 1)

        # ----- Menu -----
        self.menu_widget = MenuWidget(self.function_widget.update_widget)
        self.Grid_Layout.addWidget(self.menu_widget, 1, 0, 1, 1)

        self.Grid_Layout.setColumnStretch(0, 1)
        self.Grid_Layout.setColumnStretch(1, 6)
        self.Grid_Layout.setRowStretch(0, 1)
        self.Grid_Layout.setRowStretch(1, 6)

        self.setLayout(self.Grid_Layout)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.widget_dict = {
            'add': self.addWidget(AddStuWidget(self)),
            'show': self.addWidget(ShowStuWidget(self))
        }
        self.update_widget('add')

    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        # current_widget.load()
