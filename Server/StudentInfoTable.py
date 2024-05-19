from DBConnection import DBConnection
from DBInitializer import DBInitializer


class StudentInfoTable:
    def initial(self):
        DBConnection.db_file_path = "Student_Data.db"
        DBInitializer().execute()

    def Load_data(self, table):
        self.initial()
        command = f"SELECT * FROM {table}"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return [row['stu_id'] for row in record_from_db]

    def insert_data(self, table, col, values):
        self.initial()
        command = f"INSERT INTO {table} ({col}) VALUES ({values});"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_data(self, table, in_type, values, return_type):
        """
        :param table: student_info / subject_info
        :param in_type: stu_id / name / subject / score
        :param values: values
        :param return_type: stu_id / name / subject / score
        :return:
        """
        self.initial()
        command = f"SELECT * FROM {table} WHERE {in_type}='{values}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return [row[return_type] for row in record_from_db]

    def select_data_2_col(self, table, col, values, return_type):
        self.initial()
        command = f"SELECT * FROM {table} WHERE {col[0]}='{values[0]}' AND {col[1]}='{values[1]}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return [row[return_type] for row in record_from_db]

    def delete_data(self, table, stu_id):
        command = f"DELETE FROM {table} WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_data(self, table, change_col, change_value, col, values):
        command = f"UPDATE {table} SET {change_col}='{change_value}' WHERE {col[0]}='{values[0]}' AND {col[1]}='{values[1]}';"
        # command = "UPDATE student_info SET name='{}' WHERE stu_id='{}';".format(name, stu_id)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       