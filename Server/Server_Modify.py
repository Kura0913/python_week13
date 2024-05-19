from StudentInfoTable import StudentInfoTable


class ServerModify:
    def execute(self, message):
        subject_data = message['parameters']['scores']
        name = message['parameters']['name']
        subject = list(subject_data.keys())[0]
        score = subject_data[subject]
        stu_id = StudentInfoTable().select_data('student_info', 'name', name, 'stu_id')[0]
        if message['parameters']['status'] == 'new':
            StudentInfoTable().insert_data('subject_info', 'stu_id, subject, score',
                                           f"'{stu_id}', '{subject}', '{score}'")
        else:
            StudentInfoTable().update_data('subject_info', 'score', score, ('stu_id', 'subject'),
                                           (stu_id, subject))
        return {'status': 'OK', 'parameters': [message['parameters']['name'],
                                               subject, subject_data[subject]]}
