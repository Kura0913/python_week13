from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class DelStuServer:
    def __init__(self):  
        pass                              

    def execute(parameter):
        reply_msg = dict()
        reply_msg['status'] = 'OK'
        stu_id = StudentInfoTable().select_a_student(parameter['name'])
        
        StudentInfoTable().delete_a_student(stu_id)
        SubjectInfoTable().delete_a_subject(stu_id)
        print(f"    Del {parameter['name']} success")
        
        return reply_msg