from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class ModifyStuServer:
    def __init__(self):  
        pass                              

    def execute(parameter):
        reply_msg = dict()
        reply_msg['status'] = 'OK'
        stu_id = StudentInfoTable().select_a_student(parameter['name'])
        
        for subject, score in parameter['scores_dict'].items():
            if not SubjectInfoTable().select_a_subject(stu_id, subject):
                SubjectInfoTable().insert_a_subject(stu_id, subject, score)
                print(f"    Add {parameter['name']} success")
            elif SubjectInfoTable().select_a_subject(stu_id, subject) != score:
                SubjectInfoTable().update_a_subject(stu_id, subject, score)
                print(f"    Modify {parameter['name']} success")
        return reply_msg