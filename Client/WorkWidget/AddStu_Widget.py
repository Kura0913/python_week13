import time
import json
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFont
from WorkWidget.Widget_Components import Label, LineEdit, Button


class AddStuWidget(QtWidgets.QWidget):
    student_data = dict()

    def __init__(self, main_widget):
        super().__init__(main_widget)
        self.main_widget = main_widget

        # ========== Layout Grid ===========
        self.Grid_Layout = QtWidgets.QGridLayout()

        # ========== Add Student ===========
        self.Add_student_Label = Label(self, 'Add Student', font_size=18)
        self.Grid_Layout.addWidget(self.Add_student_Label, 0, 0, 0, 0)
        self.Grid_Layout.setRowStretch(0, 1)
        self.Grid_Layout.setColumnStretch(0, 1)

        # ========== Name ==========
        self.Name_Label = Label(self, 'Name:', font_size=16)
        self.Grid_Layout.addWidget(self.Name_Label, 1, 0, 1, 1)
        self.Grid_Layout.setRowStretch(1, 1)
        self.Grid_Layout.setColumnStretch(1, 1)

        self.Name_LineEdit = LineEdit(self, font_size=14, object_name='Name')
        self.Name_LineEdit.setText('Name')
        self.Grid_Layout.addWidget(self.Name_LineEdit, 2, 1, 1, 1)
        self.Grid_Layout.setRowStretch(2, 1)
        self.Grid_Layout.setColumnStretch(2, 1)

        # ========== Subject ==========
        # self.Subject_Label = Label(self, 'Subject:', font_size=16)
        # self.Grid_Layout.addWidget(self.Subject_Label, 3, 0, 1, 1)
        # self.Grid_Layout.setRowStretch(3, 1)
        # self.Subject_LineEdit = LineEdit(self,  font_size=14, object_name='Subject')
        # self.Subject_LineEdit.setDisabled(True)
        # self.Subject_LineEdit.setText('Subject')
        # self.Grid_Layout.addWidget(self.Subject_LineEdit, 4, 1, 1, 1)

        # ========== Score ==========
        # self.Score_Label = Label(self, 'Score:', font_size=16)
        # self.Grid_Layout.addWidget(self.Score_Label, 5, 0, 1, 1)
        # self.Score_LineEdit = LineEdit(self, font_size=14, object_name='Score')
        # self.Score_LineEdit.setDisabled(True)
        # regular_expression = QtCore.QRegularExpression('^\d{3}$')
        # validator = QtGui.QRegularExpressionValidator(regular_expression, self)
        # self.Score_LineEdit.setValidator(validator)
        # self.Grid_Layout.addWidget(self.Score_LineEdit, 6, 1, 1, 1)

        # ========== Query ==========
        # self.Query_Button = Button(self, 'Query', font_size=13, fix_size=(110, 25))
        # self.Query_Button.setDisabled(True)
        # self.Query_Button.clicked.connect(self.Query_mode)
        #
        # self.Add_Button = Button(self, 'Add', font_size=13, fix_size=(110, 25))
        # self.Add_Button.setDisabled(True)
        # self.Add_Button.clicked.connect(self.Add_mode)

        # =========== Information =============
        # self.Info_Label = Label(self, "The Information:", (420, 10), 14)
        # self.Info_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        # self.Info_Label.setStyleSheet('color: rgb(222, 71, 39)')
        # self.Info_Label.setWordWrap(True)
        # self.Info_Label.setMinimumHeight(400)
        # self.Info_Label.setMinimumWidth(280)

        # ============ Send Button =============
        # self.send_button = Button(self, 'Send', font_size=12, fix_size=(170, 30))
        # self.send_button.clicked.connect(self.Send_Data)

        self.setLayout(self.Grid_Layout)

    # ===== Send Client Data =====
    def confirm_action(self, command, parameters=None):
        self.send_command = Execute_Command(self.main_widget, command, parameters)
        self.send_command.start()
        self.send_command.return_sig.connect(self.process_result)

    def process_result(self, result):
        result = json.loads(result)
        print_text = 'The Information:\n'
        print_text += f"{result['data']}"
        self.Info_Label.setText(print_text)

        # ==== Each Mode Process ====
        # ==== Query ====
        if result['data']['status'] == 'Fail':
            if result['command'] == 'query':
                self.Subject_LineEdit.setDisabled(False)

    # ===== Function of Mode =====
    def Query_mode(self):
        self.Info_Label.clear()
        self.confirm_action('query', {'name': self.Name_LineEdit.text()})

    def Add_mode(self):
        # === Read Student Data ===
        name = self.Name_LineEdit.text()
        subject = self.Subject_LineEdit.text()
        score = self.Score_LineEdit.text()

        if len(self.student_data) != 0:
            self.student_data['scores'][subject] = score
        else:
            self.student_data = {'name': name, 'scores': {subject: score}}

        # === Clear & Set Info Label ===
        self.Info_Label.clear()
        print_text = 'The Information:\n'
        print_text += f"Student {name}'s subject '{subject}' with score '{score}' added"
        self.Info_Label.setText(print_text)

    def Send_Data(self):
        if len(self.student_data) == 0:
            print_text = ('The Information:\n'
                          'Please input the Name, Subject, Score !!')
        else:
            print_text = "The Information: is send"
        self.confirm_action('add', self.student_data)
        self.Info_Label.clear()
        self.Info_Label.setText(print_text)

        # ---- Clear ----
        self.student_data = dict()
        self.Name_LineEdit.setText('Name')

        self.Subject_LineEdit.setText('Subject')
        self.Subject_LineEdit.setDisabled(True)

        self.Score_LineEdit.clear()
        self.Score_LineEdit.setDisabled(True)

        self.Query_Button.setDisabled(True)
        self.Add_Button.setDisabled(True)

    # ===== Function of UI =====
    # def check_text(self, objects, text):
    #     if len(text) == 0:
    #         return 0
    #     if objects == 'Name':
    #         self.Query_Button.setDisabled(False)
    #     elif objects == 'Subject':
    #         self.Score_LineEdit.setDisabled(False)
    #     elif objects == 'Score':
    #         self.Add_Button.setDisabled(False)
    #
    # def check_mouse(self, objects):
    #     if objects == 'Name':
    #         self.Subject_LineEdit.setDisabled(True)
    #         self.Score_LineEdit.setDisabled(True)
    #         self.Add_Button.setDisabled(True)

    def Font_Config(self, font_size):
        font = QFont('Arial', pointSize=font_size, weight=500)
        font.setBold(True)
        return font


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
