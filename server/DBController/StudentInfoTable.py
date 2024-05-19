from DBController.DBConnection import DBConnection


class StudentInfoTable:
    
    def insert_a_student(self, name):
        command = "INSERT INTO student_info (name) VALUES  ('{}');".format(name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
            stu_id = cursor.lastrowid
        return stu_id    
    
    def insert_scores(self,stu_id, scores):
        
        with DBConnection() as connection:
            cursor = connection.cursor()
            for subject, score in scores.items():
                cursor.execute("INSERT INTO subject_info (stu_id, subject, score) VALUES ('{}', '{}', '{}');".format(stu_id, subject, score))
            connection.commit()

    def select_a_student(self, name):
        command = "SELECT * FROM student_info WHERE name='{}';".format(name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
            
        if record_from_db:
            return record_from_db[0]["stu_id"]  
        else:
            return None  
    
    def fetch_all_data(self):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM student_info")#所有學生訊息
            students_data = cursor.fetchall()

        result_dict = {}

        for student in students_data:
            name = student['name']
            stu_id = student['stu_id']

            result_dict[name] = {'name': name, 'scores': {}}
            result_dict[name]['scores']=self.fetch_student_scores(stu_id)
            
        return result_dict

    
    def fetch_student_scores(self,stu_id):
        command = "SELECT subject, score FROM subject_info WHERE stu_id='{}';".format(stu_id)
        student_scores = {}

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            scores_data = cursor.fetchall()

        for score in scores_data:#scores_data是很多的{subject:,score:}
            subject = score['subject']
            score_value = score['score']
            student_scores[subject] = score_value
        return student_scores 
        

    def delete_a_student(self, stu_id):
        
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM student_info WHERE stu_id='{}';".format(stu_id))
            cursor.execute("DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id))
            connection.commit()

    def update_student_scores(self, name,new_score_dict):

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT stu_id FROM student_info WHERE name = '{}'".format(name))
            stu_id = cursor.fetchone()[0]
            for subject, score in new_score_dict.items():
                
                cursor.execute("SELECT score FROM subject_info WHERE stu_id = '{}' AND subject = '{}'".format(stu_id, subject))# 看科目存不存在
                score_record = cursor.fetchone()

                if score_record is not None:#已經有成績，更新
                    cursor.execute("UPDATE subject_info SET score = '{}' WHERE stu_id = '{}' AND subject = '{}'".format(score, stu_id, subject))
                else:#還沒有這個科目，新增
                    cursor.execute("INSERT INTO subject_info (stu_id, subject, score) VALUES ('{}', '{}', '{}')".format(stu_id, subject, score))

            connection.commit()
       