from Server_Query import ServerQuery
from Server_Add import ServerAdd
from Server_Show import ServerShow
from Server_Delete import ServerDelete
from Server_Modify import ServerModify


class ServerPaser:
    def __init__(self):
        self.function_list = {'add': ServerAdd,
                              'query': ServerQuery,
                              'show': ServerShow,
                              'del': ServerDelete,
                              'modify': ServerModify}

    def execute(self, message):
        print(f'   server received: {message}\n')
        return self.function_list[message['command']]().execute(message)
