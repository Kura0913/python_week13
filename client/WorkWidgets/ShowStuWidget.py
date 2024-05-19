from PyQt6 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent, ScrollAreaComponent
from SocketClient.ServiceController import ExecuteConfirmCommand
import json

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Show Student")
        self.scroll = ScrollAreaComponent()

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.scroll, stretch=9)
        self.setLayout(layout)
    
    def load(self, socket_client):
        print("<<< Show Widget >>>")
        self.execution = ExecuteConfirmCommand(socket_client, "show")
        self.execution.start()
        self.execution.result_msg.connect(self.action_show)

    def action_show(self, result):
        result = json.loads(result)
        if result["status"] == "OK":
            self.setSubjectScore(result["parameters"])

    def setSubjectScore(self, parameters):
        add_content = "====student list====\n"
        for key, info in parameters.items():
            add_content += f"Name : {key}\n"
            for inner_key, inner_info in info['scores'].items():
                add_content += f"    subject : {inner_key},  scores : {inner_info}\n"
            add_content += "\n"
        self.scroll.content.setText(add_content)