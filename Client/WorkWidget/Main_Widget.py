import json
from PyQt6 import QtWidgets, QtCore
from WorkWidget.AddStu_Widget import AddStuWidget
from WorkWidget.ShowStu_Widget import ShowStuWidget
from WorkWidget.Menu_Widget import MenuWidget
from WorkWidget.Widget_Components import Label
from Client_Socket import SocketClient


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.client = SocketClient('127.0.0.1', 20001)

        # ----- Set Window Title -----
        self.setObjectName("main_widget")

        # ----- Grid Layout -----
        self.Grid_Layout = QtWidgets.QGridLayout()

        # ----- Title -----
        label = Label(self, "Student Management System", font_size=18)
        self.Grid_Layout.addWidget(label, 0, 0, 1, 2)

        # ----- Function -----
        self.function_widget = FunctionWidget(self)
        self.Grid_Layout.addWidget(self.function_widget, 1, 1, 1, 1)

        # ----- Menu -----
        self.menu_widget = MenuWidget(self.function_widget.update_widget)
        self.Grid_Layout.addWidget(self.menu_widget, 1, 0, 1, 1)

        self.Grid_Layout.setColumnStretch(0, 1)
        self.Grid_Layout.setColumnStretch(1, 6)
        self.Grid_Layout.setRowStretch(0, 1)
        self.Grid_Layout.setRowStretch(1, 6)

        self.setLayout(self.Grid_Layout)

    def confirm_action(self, process_result, command, parameters=None):
        self.send_command = Execute_Command(self, command, parameters)
        self.send_command.start()
        self.send_command.return_sig.connect(process_result)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self, main_widget):
        super().__init__()
        self.widget_dict = {
            'add': self.addWidget(AddStuWidget(main_widget)),
            'show': self.addWidget(ShowStuWidget(main_widget))
        }
        self.update_widget('add')

    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()


# ========== Execute Client Command ==========
class Execute_Command(QtCore.QThread):
    return_sig = QtCore.pyqtSignal(str)

    def __init__(self, app, command, parameters=None):
        super().__init__()
        self.app = app
        self.command = command
        self.parameters = parameters

    def run(self):
        print(f"Command: {self.command}, Parameters: {self.parameters}")
        self.app.client.send_command(self.command, self.parameters)
        _, received = self.app.client.wait_response(1940)
        result = {'command': self.command, 'data': json.loads(received)}
        self.return_sig.emit(json.dumps(result))
