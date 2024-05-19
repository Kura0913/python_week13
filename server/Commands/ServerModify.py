from DBController.StudentInfoTable import StudentInfoTable


class ServerModify():
    def __init__(self):
        pass
    def execute(self,data):
        StudentInfoTable().update_student_scores(data['name'],data['scores_dict'])
        sent_data={}
        sent_data['status'] = 'OK'
        return sent_data