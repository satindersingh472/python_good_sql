
import mariadb
import dbcreds

def connect_db():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host,port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    return cursor

def execute_statement(cursor,statement,list=[]):
    cursor.execute(statement,list)
    result = cursor.fetchall()
    return result

def close_connection(cursor):
    conn = cursor.connection
    cursor.close()
    conn.close()
