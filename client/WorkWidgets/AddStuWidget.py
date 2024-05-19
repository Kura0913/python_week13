from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.SocketClient import SocketClient 
from SocketClient.ServiceController import ExecuteConfirmCommand
import json


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self,  client:SocketClient):
        super().__init__()
        self.setObjectName("add_stu_widget")
        self.client = client
        self.add_stru = AddStru(self.client)

        # validator
        int_validator = QtGui.QIntValidator(0, 100)

        layout = QtWidgets.QGridLayout()
        # label
        header_label = LabelComponent(20, "Add Student")
        name_label = LabelComponent(16, "Name: ")
        subject_label = LabelComponent(16, "Subject:")
        score_label = LabelComponent(16, "Score:")
        self.message_label = LabelComponent(16, "")
        # editor label
        self.name_editor_label = LineEditComponent("Name")
        self.name_editor_label.mousePressEvent = self.clear_name_editor_content
        self.name_editor_label.textChanged.connect(self.name_editor_text_changed)
        
        self.subject_editor_label = LineEditComponent("Subject")
        self.subject_editor_label.mousePressEvent = self.clear_subject_editor_content
        self.subject_editor_label.setEnabled(False)

        self.score_editor_label = LineEditComponent("")
        self.score_editor_label.setValidator(int_validator)
        self.score_editor_label.setEnabled(False)

        # button
        self.query_button = ButtonComponent("Query")
        self.query_button.setEnabled(False)
        self.query_button.clicked.connect(self.query_action)        

        self.add_button = ButtonComponent("Add")
        self.add_button.setEnabled(False)
        self.add_button.clicked.connect(self.add_action)

        self.send_button = ButtonComponent("Send")
        self.send_button.setEnabled(True)
        self.send_button.clicked.connect(self.send_action)

        # set label layout
        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.message_label, 1, 3, 10, 10)
        # set editor label layout
        layout.addWidget(self.name_editor_label, 1, 1, 1, 1)
        layout.addWidget(self.subject_editor_label, 2, 1, 1, 1)
        layout.addWidget(self.score_editor_label, 3, 1, 1, 1)
        # set button layout
        layout.addWidget(self.query_button, 1, 2, 1, 1)
        layout.addWidget(self.add_button, 3, 2, 1, 1)
        layout.addWidget(self.send_button, 5, 3, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 2)
        layout.setColumnStretch(3, 4)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 2)
        self.setLayout(layout)

    def load(self):
        print("add widget")

    def clear_name_editor_content(self, event):
        self.name_editor_label.clear()

    def clear_subject_editor_content(self, event):
        self.subject_editor_label.clear()

    # name editor label text changed event
    def name_editor_text_changed(self, text):
        self.name_editor_label.setText(text)

        if text == 'Name' or text == '':
            self.query_button.setEnabled(False)
        else:
            self.query_button.setEnabled(True)

    # query button clicked event
    def query_action(self):
        self.send_command = ExecuteConfirmCommand(self.client, "query", {"name" : self.name_editor_label.text()})
        self.send_command.start()
        self.send_command.result_msg.connect(self.query_action_result)
    # get query result
    def query_action_result(self, result):
        result_message = json.loads(result)
        
        if result_message['status'] == "Fail": # status: Fail means the name can be added.
            self.message_label.setText(f"Query success")
            self.message_label.set_color("green")
            self.add_stru.add_name(self.name_editor_label.text())
            self.setWidgetEnable(False, True, True, False)
        else: # status: OK means the name is already in the database.
            print(f"The name {self.name_editor_label.text()} is already in the list.")
            self.message_label.setText(f"The name {self.name_editor_label.text()} is already in the list.")
            self.message_label.set_color("red")
            self.name_editor_label.setText("Name")

    # add button clicked event
    def add_action(self):
        if self.subject_editor_label.text() != '' and self.subject_editor_label.text() != 'Subject' and self.score_editor_label.text() != '':
            self.add_stru.add_subject_and_score(self.subject_editor_label.text(), self.score_editor_label.text())
            self.message_label.setText(f"add {self.subject_editor_label.text()} : {self.score_editor_label.text()}")
            self.message_label.set_color('green')
            self.subject_editor_label.setText('')
            self.score_editor_label.setText('')
        else:
            print("Please input subject and score.")
            self.message_label.setText("Please input subject and score.")
            self.message_label.set_color("red")

    # send button clicked event
    def send_action(self):
        if self.name_editor_label.text() != "Name" and not self.query_button.isEnabled() and self.add_stru.parameters:
            self.send_command = ExecuteConfirmCommand(self.client, "add", self.add_stru.parameters)
            self.send_command.start()
            self.send_command.result_msg.connect(self.send_action_result)
    
    # get add execute result
    def send_action_result(self, result):
        result_message = json.loads(result)
        if result_message["status"] == "OK":
            self.message_label.set_color("green")
            self.message_label.setText(f"{self.add_stru.parameters['name']}'s sbjects and score save success.")
            self.add_stru.reset_parameters()
            self.setWidgetEnable(True, False, False, False)

    # widget enable setting
    def setWidgetEnable(self, name_editor_enable=True, subject_and_score_editor_enable=True, add_btn_enable=True, query_btn_enable=True):
        self.name_editor_label.setEnabled(name_editor_enable)
        self.subject_editor_label.setEnabled(subject_and_score_editor_enable)
        self.score_editor_label.setEnabled(subject_and_score_editor_enable)
        self.add_button.setEnabled(add_btn_enable)
        self.query_button.setEnabled(query_btn_enable)

class AddStru():
    def __init__(self, client:SocketClient):
        self.parameters = {}
        self.client = client
    
    def show_result(self, res):
        if res['status'] == 'OK':
            print(f"Add {self.parameters} success")
        else:
            print(f"Add {self.parameters} fail")
    
    def add_name(self, name):
        self.parameters['name'] = name
        self.parameters['scores'] = {}

    def add_subject_and_score(self, subject, score):
        if 'scores' not in self.parameters.keys():
            self.parameters['scores'] = {}
        self.parameters['scores'][subject] = score
    
    def reset_parameters(self):
        self.parameters.clear()