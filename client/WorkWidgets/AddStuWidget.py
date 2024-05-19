from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
import threading

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.info_dict = dict()
        self.setObjectName("add_stu_widget")
        self.layout = QtWidgets.QGridLayout()
        
        #score_editor's setting
        validator = QtGui.QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator.setBottom(0)
        
        header_label = LabelComponent(20, "Add Student")
        self.layout.addWidget(header_label, 0, 0, 2, 2)
        
        #Name
        self.name_label = self.create_label(16, "Name: ", 1, 0)
        self.name_editor = self.create_editor("Name", 1, 1)
        #Subject
        self.subject_label = self.create_label(16, "Subject: ", 2, 0)
        self.subject_editor = self.create_editor("Subject", 2, 1, self.name_editor)
        #Score
        self.score_label = self.create_label(16, "Score: ", 3, 0)
        self.score_editor = self.create_editor("", 3, 1, self.subject_editor)
        self.score_editor.setValidator(validator)
        #Query button
        self.query_button = self.create_button("Query", 1, 2, self.query_action, self.name_editor)
        #Add button
        self.add_button = self.create_button("Add", 3, 2, self.add_action, self.score_editor)
        #Send button
        self.send_button = self.create_button("Send", 5, 3, self.send_action)   
        #Hint
        self.hint_label = self.create_label(12, "", 0, 3, "red", 200, 2)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 2)
        self.layout.setColumnStretch(2, 1)
        self.layout.setColumnStretch(3, 2)

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(3, 1)
        self.layout.setRowStretch(4, 4)
        self.layout.setRowStretch(5, 1)

        self.setLayout(self.layout)
        
    def create_label(self, font_size, context, row, column, color="black", length=None, row_cross=1):
        new_label = LabelComponent(font_size, context, color, length)
        self.layout.addWidget(new_label, row, column, row_cross, 1)
        return new_label
                
    def create_editor(self, name, row, column, toggle_editor=None):
        new_editor = LineEditComponent(name)
        self.layout.addWidget(new_editor, row, column, 1, 1)
        if toggle_editor:
            new_editor.setEnabled(False)
            toggle_editor.textChanged.connect(lambda: self.toggle_editor_state(toggle_editor, new_editor))   
        return new_editor  
    
    def create_button(self, name, row, column, action, toggle_editor=None):
        new_button = ButtonComponent(name)
        self.layout.addWidget(new_button, row, column, 1, 1)
        new_button.clicked.connect(action)
        if toggle_editor:
            new_button.setEnabled(False)
            toggle_editor.textChanged.connect(lambda: self.toggle_button_state(new_button, toggle_editor))  
        return new_button  
    
    def query_action(self):
        threading.Thread(target = self.query_action_thread).start()
                  
    def query_action_thread(self):
        self.client.send_command('query', {'name':self.name_editor.text()}) 
        if self.client.receive_data()['status'] == 'Fail':
            self.hint_label.setText(f"Please enter subjects for student '{self.name_editor.text()}'")
            self.query_button.setEnabled(False)
            self.subject_editor.setEnabled(True)
        else:
            self.hint_label.setText(f"The name {self.name_editor.text()} already exists.'")

    def add_action(self):
        if self.info_dict:
            if self.info_dict['name'] != self.name_editor.text():
                self.info_dict['name'] = self.name_editor.text()
                self.info_dict['scores'] = {}
        else:
            self.info_dict['name'] = self.name_editor.text()
            self.info_dict['scores'] = {}
        
        if self.subject_editor.text() in self.info_dict['scores']:
            self.hint_label.setText(f"{self.subject_editor.text()} already exists")    
        else:   
            try: 
                self.info_dict['scores'][self.subject_editor.text()] = float(self.score_editor.text())
            except:
                pass
            self.hint_label.setText(f"Student {self.name_editor.text()}'s subject '{self.subject_editor.text()}' with score '{self.score_editor.text()}' added")
        
        self.reset()
        self.subject_editor.setText("Subject")
    
    def send_action(self):
        threading.Thread(target = self.send_action_thread).start()
    
    def send_action_thread(self):
        if not self.info_dict:
            self.hint_label.setText("Please enter the student information and add it.")
            return
        
        self.client.send_command('add', self.info_dict)
        if self.client.receive_data()['status'] == 'OK':
            self.hint_label.setText(f"The information {self.info_dict} is sent.")
            self.name_editor.setText("Name")
            self.reset()
            self.info_dict = {}
        else:
            self.hint_label.setText(f"Add fail.")
        
    def toggle_button_state(self, button, line_edit):
        button.setEnabled(bool(line_edit.text() and line_edit.text() != "Name"))    
    
    def toggle_editor_state(self, current_editor, next_editor):
        if current_editor.text() and current_editor.isEnabled() and current_editor != self.name_editor and current_editor.text() != "Subject":
            next_editor.setEnabled(True)
        else: 
            self.reset()
    
    def reset(self):
        if not self.name_editor.text() or self.name_editor.text() == "Name":
            self.subject_editor.setText("Subject")
            self.subject_editor.setEnabled(False)
        self.score_editor.setText("")
        self.score_editor.setEnabled(False)  