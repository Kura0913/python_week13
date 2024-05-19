from Server_Socket import Server_Socket


if __name__ == '__main__':
    Server = Server_Socket('127.0.0.1', 20001)
    Server.daemon = True
    Server.serve()

    while True:
        command = input()
        if command == 'finish':
            break
    Server.server_socket.close()
    print('Server Close')
