import sqlite3 as sql


connection = sql.connect('calender.db', check_same_thread=False)
cursor = connection.cursor()


def execute_query(query):
    return cursor.execute(query)


def execute_insert(query):
    execute_query(query)
    connection.commit()
