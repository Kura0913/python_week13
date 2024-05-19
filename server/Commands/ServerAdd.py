from DBController.StudentInfoTable import StudentInfoTable

class ServerAdd():
    def __init__(self):
        pass
    def execute(self,data):#收到的data是要新加的資料
        sent_data={}
        stu_id=StudentInfoTable().insert_a_student(data['name'])
        StudentInfoTable().insert_scores(stu_id, data['scores'])
        sent_data['status'] = 'OK'
       
        return sent_data       