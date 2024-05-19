from PyQt6 import QtWidgets, QtGui, QtCore


class Button(QtWidgets.QPushButton):
    def __init__(self, window, text, position=(0, 0), font_size=10, fix_size=(110, 25)):
        super().__init__(window)
        self.setText(text)
        self.setFixedSize(fix_size[0], fix_size[1])
        self.move(position[0], position[1])
        self.setFont(Font_Config(font_size))


class Label(QtWidgets.QLabel):
    def __init__(self, window, text, position=(0, 0), font_size=10):
        super().__init__(window)
        self.setText(text)
        self.move(position[0], position[1])
        self.setFont(Font_Config(font_size))
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)


class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, windows, position=(0, 0), font_size=10, fix_size=(170, 25), object_name='default'):
        super().__init__(windows)
        self.windows = windows
        self.setObjectName(object_name)
        self.setFixedSize(fix_size[0], fix_size[1])
        self.move(position[0], position[1])
        self.setFont(Font_Config(font_size))
    #     self.textEdited.connect(self.return_text)
    #
    # def return_text(self, text):
    #     self.windows.check_text(self.objectName(), text)
    #
    # def mousePressEvent(self, a0):
    #     self.clear()
    #     self.windows.check_mouse(self.objectName())

def Font_Config(font_size):
    font = QtGui.QFont('Arial', pointSize=font_size, weight=500)
    font.setBold(True)
    return font


