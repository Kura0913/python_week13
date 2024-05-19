from PyQt6 import QtWidgets, QtCore, QtGui


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content,color='black',alignment=QtCore.Qt.AlignmentFlag.AlignLeft,resizable=False,width=2000):
        super().__init__()

        self.setMaximumWidth(width)
        self.setWordWrap(True)
        self.setAlignment(alignment)

        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=500))
        self.setText(content)
        self.setStyleSheet(f"color: {color};")

        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(resizable)
        self.scroll_area.setWidget(self)



class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=150,height=30, font_size=16,enable=True, regex=None):
        super().__init__()
        self.default_content = default_content
        self.default_length = length
        self.default_width = width
        self.default_height = height
        self.default_font_size = font_size
        self.default_enable = enable
        self.regex=regex

        self.initUI(regex)

    def initUI(self,regex):
        self.setMaxLength(self.default_length)
        self.setText(self.default_content)

        self.setFixedWidth(self.default_width)
        self.setFixedHeight(self.default_height)
        self.setFont(QtGui.QFont("Arial", self.default_font_size))
        self.setEnabled(self.default_enable)
       
        if regex is not None:
            regular_expression = QtCore.QRegularExpression(regex)
            validator = QtGui.QRegularExpressionValidator(regular_expression, self)
            self.setValidator(validator)
        
    def mousePressEvent(self, event):
        super().mousePressEvent(event)  
        self.clear()  
    def reset(self):
        self.initUI(self.regex)
    
        
class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16,enable=False):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setEnabled(enable)

