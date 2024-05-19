from DBController.StudentInfoTable import StudentInfoTable


class ServerShow():
    def __init__(self):
        pass
    def execute(self,data):
        sent_data={}
        sent_data['status'] = 'OK'
        sent_data['parameters']=StudentInfoTable().fetch_all_data()
        return sent_data