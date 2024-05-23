from PyQt6 import QtWidgets
from WorkWidget.Main_Widget import MainWidget
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_windows = MainWidget()
    main_windows.setFixedSize(800, 500)
    main_windows.setWindowTitle('Student System Client')
    main_windows.show()
    sys.exit(app.exec())
