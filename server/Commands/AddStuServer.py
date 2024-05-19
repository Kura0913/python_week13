from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class AddStuServer:
    def __init__(self):  
        pass                              

    def execute(parameter):
        reply_msg = dict()
        reply_msg['status'] = 'OK'
        reply_msg['parameters'] = parameter
        
        StudentInfoTable().insert_a_student(parameter['name'])
        stu_id = StudentInfoTable().select_a_student(parameter['name'])
        for subject, score in parameter['scores'].items():
            SubjectInfoTable().insert_a_subject(stu_id, subject, score)
        
        return reply_msg