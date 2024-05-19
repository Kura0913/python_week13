from StudentInfoTable import StudentInfoTable


class ServerQuery:
    def execute(self, message):
        name = message['parameters']['name']
        student_id = StudentInfoTable().select_data('student_info', 'name', name, 'stu_id')
        if len(student_id) != 0:
            data = {'name': name, 'scores': dict()}
            subjects = StudentInfoTable().select_data('subject_info', 'stu_id', student_id[0], 'subject')
            scores = StudentInfoTable().select_data('subject_info', 'stu_id', student_id[0], 'score')
            for subject, score in zip(subjects, scores):
                data['scores'][subject] = score
            return {'status': 'OK', 'parameters': data}
        else:
            return {'status': 'Fail', 'reason': 'The name is not found'}
