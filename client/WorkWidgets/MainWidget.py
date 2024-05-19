from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent

class MainWidget(QtWidgets.QWidget):
    def __init__(self, client):
        super().__init__()
        self.setObjectName("main_widget")
        
        #lower right part
        lower_right_widget = QtWidgets.QStackedWidget()
        add_stu_widget = AddStuWidget(client)
        show_stu_widget = ShowStuWidget(client)
        lower_right_widget.addWidget(add_stu_widget)
        lower_right_widget.addWidget(show_stu_widget)
        
        #lower left part
        lower_left_layout = QtWidgets.QVBoxLayout()
        lower_left_widget = QtWidgets.QWidget()
        add_button = ButtonComponent("Add student")
        show_button = ButtonComponent("Show all")
        lower_left_layout.addWidget(add_button)
        lower_left_layout.addWidget(show_button)
        lower_left_widget.setLayout(lower_left_layout)
        add_button.clicked.connect(lambda: lower_right_widget.setCurrentWidget(add_stu_widget))
        show_button.clicked.connect(show_stu_widget.show_action)
        show_button.clicked.connect(lambda: lower_right_widget.setCurrentWidget(show_stu_widget))
        
        #lower part
        lower_layout = QtWidgets.QHBoxLayout()
        lower_widget = QtWidgets.QWidget()
        lower_layout.addWidget(lower_left_widget, stretch=22)
        lower_layout.addWidget(lower_right_widget, stretch=78)
        lower_widget.setLayout(lower_layout)
    
        main_layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(24, "Student Management System")
        main_layout.addWidget(header_label, stretch=13)
        main_layout.addWidget(lower_widget, stretch=87)

        self.setLayout(main_layout)