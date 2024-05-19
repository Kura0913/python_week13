from SocketClient.SocketClient import SocketClient
from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
import sys

host = "127.0.0.1"
port = 20001

if __name__ == '__main__':
    client = SocketClient(host, port)
    
    app = QApplication([])
    main_window = MainWidget(client)
    main_window.setFixedSize(900, 400)
    main_window.show()

    sys.exit(app.exec())