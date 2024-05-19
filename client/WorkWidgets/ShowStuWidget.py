from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
import threading

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.setObjectName("show_stu_widget")
        self.layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(20, "Show Student")
        self.text_area = QtWidgets.QTextEdit()
        self.text_area.setReadOnly(True)
        
        #Scroll
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(self.text_area)
        self.scroll_area.setWidgetResizable(True)
        
        self.layout.addWidget(header_label, stretch=11)
        self.layout.addWidget(self.scroll_area, stretch=89)
        self.setLayout(self.layout) 
        
    def show_action(self):
        self.client.send_command('show', {})
        self.student_dict = self.client.receive_data()['parameters']

        student_info = "==== student list ====\n"
        for name, student_info_dict in self.student_dict.items():
            student_info += f"Name: {name}\n"
            for subject, score in student_info_dict['scores'].items():
                student_info += f"  Subject: {subject}, score: {score}\n"
            student_info += "\n"

        self.text_area.setText(student_info)