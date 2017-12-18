import pymysql
import dbconfig


class DBHelper:

    def __init__(self, database):
        self.database = database


    def connect(self):
        return pymysql.connect(
            host=dbconfig.db_host,
            user=dbconfig.db_user,
            passwd=dbconfig.db_password,
            db=self.database
        )

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT * FROM test;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()