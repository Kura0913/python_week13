from StudentInfoTable import StudentInfoTable


class ServerShow:
    def __init__(self):
        pass

    def execute(self, x):
        parameters = dict()
        student_id_list = StudentInfoTable().Load_data('student_info')
        for stu_id in student_id_list:
            name = StudentInfoTable().select_data('student_info', 'stu_id', stu_id, 'name')[0]
            parameters[name] = {'name': name, 'scores': dict()}
            subject_list = StudentInfoTable().select_data('subject_info', 'stu_id', stu_id, 'subject')
            for subject in subject_list:
                score = StudentInfoTable().select_data_2_col('subject_info', ('stu_id', 'subject'),
                                                             (stu_id, subject),
                                                             'score')
                parameters[name]['scores'][subject] = score[0]
        return {'status': 'OK', 'parameters': parameters}

