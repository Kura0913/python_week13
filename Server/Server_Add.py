from StudentInfoTable import StudentInfoTable


class ServerAdd:
    def execute(self, message):
        parameters = message['parameters']
        name = parameters['name']
        StudentInfoTable().insert_data('student_info', 'name', f"'{name}'")
        stu_id = StudentInfoTable().select_data('student_info', 'name', name, 'stu_id')
        for scores in parameters['scores'].items():
            StudentInfoTable().insert_data('subject_info', 'stu_id, subject, score',
                                           f"'{stu_id[0]}', '{scores[0]}', '{scores[1]}'")
        return {'status': 'OK'}

    def find_index(self, data):
        num = 0
        if len(data) == 0:
            return num + 1
        for num in range(data[-1]):
            if num + 1 != data[num]:
                return num + 1
        return num + 2
