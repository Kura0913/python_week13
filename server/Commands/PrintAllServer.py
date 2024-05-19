from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class PrintAllServer:
    def __init__(self):
        pass

    def execute(parameter):
        reply_msg = dict()
        student_dict = dict()
        for stu_id, name in StudentInfoTable().select_all_student().items():
            student_dict[name] = {"name": name, "scores": SubjectInfoTable().select_all_subject(stu_id)}
            
        reply_msg['status'] = 'OK'
        reply_msg['parameters'] = student_dict
        return reply_msg