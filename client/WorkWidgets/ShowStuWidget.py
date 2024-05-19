from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from WorkWidgets.AddStuWidget import ExecuteCommand

import time
from PyQt6.QtCore import pyqtSignal
import json
import sys

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self,client):
        super().__init__()
        self.setObjectName("show_stu_widget")
        self.client = client

        layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(20, "Show Student")
        
        self.show_content = LabelComponent(12,"",resizable=True)  
        

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.show_content.scroll_area, stretch=9)
        

        self.setLayout(layout)
    def load(self):
        self.send_command = ExecuteCommand(self.client,"show",{})
        self.send_command.start()
        self.send_command.return_sig.connect(self.show_result)
    
    def show_result(self, result):
        result = json.loads(result)
        if result['status']=="OK":
            content=" ==== student list ====\n"
            for name, info in result['parameters'].items():
                content+=f"Name: {name}\n"
                for subject, score in info['scores'].items():
                    content+=f"  subject: {subject}, score: {score}\n"
                content+="\n"
            content+="======================"
            self.show_content.setText(content)
