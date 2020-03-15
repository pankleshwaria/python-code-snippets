import logging
import sqlite3
from sqlite3 import Error

logging.basicConfig(level=logging.DEBUG, format='%(name)s : %(levelname)s : %(message)s')


def get_connection(db_name):
    try:
        conn = sqlite3.connect(db_name)
        logging.debug(f'{db_name} created')
        return conn
    except Error as e:
        logging.error("Database Error: " % e.args[0])


def create_student_table(db_conn):
    try:

        sql = '''CREATE TABLE students(
                    id INTEGER,
                    name TEXT,
                    email TEXT)'''

        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        logging.debug(f"Table students created")
    except Error as e:
        logging.error("Error: %s" % e.args[0])


def create_course_table(db_conn):
    try:

        sql = '''CREATE TABLE courses(
                    id INTEGER,
                    roll_no INTEGER)'''

        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        logging.debug(f"Table courses created")
    except Error as e:
        logging.error("Error: %s" % e.args[0])


def create_record(db_conn, table_name, *records):
    try:

        if 'students' == table_name:
            sql = f'INSERT INTO {table_name} VALUES(?, ?, ?)'
        else:
            sql = f'INSERT INTO {table_name} VALUES(?, ?)'

        cursor = db_conn.cursor()
        cursor.execute(sql, records)
        db_conn.commit()
        logging.debug("Your record has been successfully added.")
    except Error as e:
        logging.error("Failed to add new record. Error %s" % e.args[0])


def fetch_record_by_id(db_conn, table_name, record_id):

    try:

        sql = f'SELECT * FROM {table_name} WHERE id = ?'
        cursor = db_conn.cursor()
        result_set = cursor.execute(sql, (record_id, ))
        return result_set.fetchall()
    except Error as e:
        logging.error("Error %s" % e.args[0])


def update_record_by_id(db_conn, table_name, record_id, name, email):

    try:
        sql = f'UPDATE {table_name} SET name = ?, email = ? where id = ?'
        cursor = db_conn.cursor()
        cursor.execute(sql, (name, email, record_id))
        db_conn.commit()
        logging.debug(f'{table_name} record with id {record_id} updated successfully')
    except Error as e:
        logging.error("Error: %s" % e.args[0])


def delete_record_by_id(db_conn, table_name, record_id):

    try:
        sql = f'DELETE FROM {table_name} WHERE id = ?'
        cursor = db_conn.cursor()
        cursor.execute(sql, (record_id, ))
        db_conn.commit()
        logging.debug(f"Record with id {record_id} deleted successfully.")
    except Error as e:
        logging.error("Error: %s" % e.args[0])


def fetch_all_records(db_conn, table_name):
    try:
        sql = f'SELECT * FROM {table_name}'
        cursor = db_conn.cursor()
        result_set = cursor.execute(sql)
        return result_set.fetchall()
    except Error as e:
        logging.error("Error: %s" % e.args[0])


conn = get_connection('my_database.db')
create_student_table(conn)
create_course_table(conn)
create_record(conn, 'students', 1, 'Percy', 'percy@gmail.lcl')
result = fetch_record_by_id(conn, 'students', 1)
print(result)
update_record_by_id(conn, 'students', 1, 'Bobby', 'iambobby@gmail.lcl')
result = fetch_record_by_id(conn, 'students', 1)
print(result)
delete_record_by_id(conn, 'students', 1)
result = fetch_all_records(conn, 'students')
print(result)

