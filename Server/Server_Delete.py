from StudentInfoTable import StudentInfoTable


class ServerDelete:
    def execute(self, message):
        name = message['parameters']['name']
        stu_id = StudentInfoTable().select_data('student_info', 'name', name, 'stu_id')[0]
        StudentInfoTable().delete_data('student_info', stu_id)
        StudentInfoTable().delete_data('subject_info', stu_id)
        return {'status': 'OK'}
