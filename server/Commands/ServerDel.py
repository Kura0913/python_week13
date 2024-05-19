from DBController.StudentInfoTable import StudentInfoTable


class ServerDel():
    def __init__(self):
        pass
    def execute(self,data):
        sent_data={}
        stu_id=StudentInfoTable().select_a_student(data['name'])
        StudentInfoTable().delete_a_student(stu_id)
        sent_data['status'] = 'OK'
        return sent_data