from DBController.StudentInfoTable import StudentInfoTable

class ServerQuery():
    def __init__(self):
        pass
    def execute(self,data):#收到的data是要新加的資料
        sent_data={}
        stu_id=StudentInfoTable().select_a_student(data['name'])
        if stu_id==None:
            sent_data['status'] = 'Fail'
            sent_data['reason']='The name is not found.'
        else:
            sent_data['status'] = 'OK'
            sent_data['scores'] = StudentInfoTable().fetch_student_scores(stu_id)
            
        
        
        return sent_data       