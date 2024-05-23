import json
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFont
from WorkWidget.Widget_Components import Label, LineEdit, Button


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, main_widget):
        super().__init__(main_widget)
        self.main_widget = main_widget
        self.grid_layout = QtWidgets.QGridLayout()

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)

        title_label = Label(self, 'Show Student', font_size=18)
        self.content = Label(self, '', font_size=14)
        self.content.setWordWrap(True)

        scroll_area.setWidget(self.content)

        self.grid_layout.addWidget(title_label, 0, 0, 6, 8)
        self.grid_layout.addWidget(scroll_area, 1, 0, 1, 7)
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 6)
        # self.grid_layout.setColumnStretch(3, 1)
        self.setLayout(self.grid_layout)

    def load(self):
        self.main_widget.confirm_action(self.process_result, 'show')

    def process_result(self, result):
        result = json.loads(result)['data']['parameters']
        show_text = '======= Student Data =======\n'
        for name in result:
            show_text += f'Name: {name}\n'
            for scores in result[name]['scores']:
                show_text += f"  Subject: {scores}   Score: {result[name]['scores'][scores]}\n"
            show_text += '\n'
        show_text += '============================'
        self.content.setText(show_text)
