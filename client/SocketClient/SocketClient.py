import socket 
import json

BUFFER_SIZE = 1940

class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))

    def send_command(self, command,parameters):
        send_data = {'command': command,'parameters': parameters}
        self.client_socket.send(json.dumps(send_data).encode())
        print(f"The client sent data =>{send_data}")

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        message = json.loads(raw_data)
        print(f"The client received data =>{message}")
        return message
        
        

    