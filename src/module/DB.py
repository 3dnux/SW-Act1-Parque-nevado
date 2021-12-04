import string


class DB:

    @classmethod
    def get(cls, query_sql: string) -> any:
        connection = psycopg2.connect(user="postgres",
                                      password="Udel$2021$1808Udel",
                                      host="159.89.129.181",
                                      port="5432",
                                      database="postgres_db")
        cursor = connection.cursor()
        cursor.execute(query_sql)
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
