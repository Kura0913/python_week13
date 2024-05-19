from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
import time

from PyQt6.QtCore import pyqtSignal
import json



class AddStuWidget(QtWidgets.QWidget):
    def __init__(self,client):
        super().__init__()
        self.setObjectName("add_stu_widget")
        self.stu_dict= {
                            'name': "",
                            'scores': {}
                        }
        self.client = client
        layout = QtWidgets.QGridLayout()
        
        header_label = LabelComponent(20,"Add Student",alignment=QtCore.Qt.AlignmentFlag.AlignVCenter)
        name_label = LabelComponent(16, "Name: ")
        subject_label = LabelComponent(16, "Subject: ")
        score_label = LabelComponent(16, "Score: ")
        self.info_label = LabelComponent(16, "",'green',width=200)
        self.info_label.setFixedWidth(200)
        self.info_label.setFixedHeight(300)

        self.editor_name_label = LineEditComponent("Name")
        self.editor_subject_label = LineEditComponent("Subject",enable=False)
        self.editor_score_label = LineEditComponent("",enable=False, regex="^\d{3}$")
        self.editor_name_label.textChanged.connect(self.editor_name_change_action)
        self.editor_subject_label.textChanged.connect(self.add_enable)
        self.editor_score_label.textChanged.connect(self.add_enable)
        #self.editor_name_label.mousePressEvent = self.editor_enable()
        

        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")
        self.send_button = ButtonComponent("Send",enable=False)
        self.query_button.clicked.connect(self.query_action)
        self.add_button.clicked.connect(self.add_action)
        self.send_button.clicked.connect(self.send_action)

        layout.addWidget(header_label, 0, 0, 1, 3)
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.info_label, 0, 4, 5, 1)

        layout.addWidget(self.editor_name_label, 1, 1, 1, 1)
        layout.addWidget(self.editor_subject_label, 2, 1, 1, 1)
        layout.addWidget(self.editor_score_label, 3, 1, 1, 1)

        layout.addWidget(self.query_button, 1, 2, 1, 1)
        layout.addWidget(self.add_button, 3, 2, 1, 1)
        layout.addWidget(self.send_button, 5, 4, 1, 1)
        
        layout.setColumnStretch(0, 10)
        layout.setColumnStretch(1, 20)
        layout.setColumnStretch(2, 10)
        layout.setColumnStretch(3,3)
        layout.setColumnStretch(4,20)
        

        layout.setRowStretch(0, 10)
        layout.setRowStretch(1, 10)
        layout.setRowStretch(2, 10)
        layout.setRowStretch(3, 10)
        layout.setRowStretch(4, 20)
        layout.setRowStretch(5, 10)

        self.setLayout(layout)
    def editor_name_change_action(self):
        if self.editor_name_label.text()!="":
            self.query_button.setEnabled(True) 
        else:
            self.query_button.setEnabled(False)
            self.editor_subject_label.reset()
            self.editor_score_label.reset() 
       
    def add_enable(self):
        if all([self.editor_name_label.text(), self.editor_subject_label.text(), self.editor_score_label.text()]):
            self.add_button.setEnabled(True) 
        else:
            self.add_button.setEnabled(False) 
    
    def query_action(self):
        self.stu_dict['name']= self.editor_name_label.text()
        self.send_command = ExecuteCommand(self.client,"query",self.stu_dict)
        self.send_command.start()
        self.send_command.return_sig.connect(self.query_result)
  
    def query_result(self, result):
        result = json.loads(result)
        if result['status']=="OK":#已經有了 不加
            self.info_label.setStyleSheet(f"color: red;")
            self.info_label.setText(f"{self.editor_name_label.text()} already exists")
        else:   
            self.stu_dict['name']=self.editor_name_label.text() 
            self.editor_subject_label.setEnabled(True)
            self.editor_score_label.setEnabled(True)
            self.send_button.setEnabled(True)
            self.info_label.setStyleSheet(f"color: green;")
            self.info_label.setText("OK")

    def add_action(self):
        
        if self.editor_subject_label.text() in self.stu_dict['scores']:
                self.info_label.setStyleSheet(f"color: red;")
                self.info_label.setText(f"{self.editor_subject_label.text()} already exists. Please input a different subject name.")
        else:
            self.info_label.setStyleSheet(f"color: green;")
            self.stu_dict['scores'][self.editor_subject_label.text()]=self.editor_score_label.text()
            self.info_label.setText(f"Student {self.stu_dict['name']}'s subject '{self.editor_subject_label.text()}' with score '{self.editor_score_label.text()}' added")
    
    def send_action(self):
        if self.stu_dict['scores']=={}:
            self.info_label.setStyleSheet(f"color: red;")
            self.info_label.setText("Please input subject and score you want to add")
        else:
            self.send_command = ExecuteCommand(self.client,"add",self.stu_dict)
            self.send_command.start()
            self.send_command.return_sig.connect(self.send_result)
    def send_result(self, result):
        result = json.loads(result)
        if result['status']=="OK":#add success
            self.info_label.setStyleSheet(f"color: green;")
            self.info_label.setText(f"The information {self.stu_dict} is sent.")
            self.reset()

    def reset(self):
        self.stu_dict= {
                            'name': "",
                            'scores': {}
                        }
        self.editor_name_label.reset()
        self.editor_subject_label.reset()
        self.editor_score_label.reset()
        self.add_button.setEnabled(False)
        self.query_button.setEnabled(False)
        self.send_button.setEnabled(False)
        self.editor_subject_label.setEnabled(False)
        self.editor_score_label.setEnabled(False)
    def load(self):
        pass

class ExecuteCommand(QtCore.QThread):
    return_sig = pyqtSignal(str)
    def __init__(self,client, command,stu_dict):
        super().__init__()
        self.client=client
        self.command=command
        self.stu_dict=stu_dict
    def run(self):
        self.client.send_command(self.command,self.stu_dict)
        result_dict = self.client.wait_response()
        self.return_sig.emit(json.dumps(result_dict))
       

        