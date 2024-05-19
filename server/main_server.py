from SocketServer.SocketServer import SocketServer
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer
from Commands.ServerAdd import ServerAdd
from Commands.ServerShow import ServerShow
from Commands.ServerQuery import ServerQuery
from Commands.ServerModify import ServerModify
from Commands.ServerDel import ServerDel


action_list = {
    "add": ServerAdd,  
    "show": ServerShow,
    "query": ServerQuery,
    "delete": ServerDel,
    "modify": ServerModify
}

class JobDispatcher:
    
    def job_execute(self,command,parameters):
        execute_result=action_list[command]().execute(parameters)
        return execute_result
    

if __name__ == '__main__':

    DBConnection.db_file_path = "example.db"
    DBInitializer().execute()
    job_dispatcher=JobDispatcher()

    server = SocketServer(job_dispatcher)
    server.daemon = True
    server.serve()
    
    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    print("leaving ....... ")   
