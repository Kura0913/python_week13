from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class QueryServer:
    def __init__(self):  
        pass                              
    
    def execute(parameter):
        reply_msg = dict()
        stu_id = StudentInfoTable().select_a_student(parameter['name'])

        if stu_id:
            reply_msg['status'] = 'OK'
            reply_msg['scores'] = SubjectInfoTable().select_all_subject(stu_id)
            print(f"    Query {parameter['name']} success")
        else:
            reply_msg['status'] = 'Fail'
            reply_msg['reason'] = 'The name is not found.'
        return reply_msg