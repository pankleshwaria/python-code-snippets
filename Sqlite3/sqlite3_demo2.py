import logging
import sqlite3
from sqlite3 import Error
from employee import Employee

logging.basicConfig(level=logging.DEBUG, format='%(name)s : %(levelname)s : %(message)s')


try:
    conn = sqlite3.connect('employee_database.db')
    cursor = conn.cursor()
except Error as e:
    logging.error("Database Error: " % e.args[0])


def insert_emp(emp):
    try:
        with conn:
            cursor.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp.first, emp.last, emp.pay))
            conn.commit()
    except Error as e:
        logging.error("Error: %s" % e)


def get_emps_by_name(lastname):
    try:
        with conn:
            cursor.execute("SELECT * FROM employees WHERE last = ?", (lastname, ))
            return cursor.fetchall()
    except Error as e:
        logging.error("Error: %s" % e)


def update_pay(emp, pay):
    try:
        with conn:
            cursor.execute("UPDATE employees SET pay = ? WHERE first = ? AND last = ?",
                           (pay, emp.first, emp.last))
            conn.commit()
    except Error as e:
        logging.error("Error: %s" % e)


def remove_emp(emp):
    try:
        with conn:
            cursor.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                           {"first": emp.first, "last": emp.last})
            conn.commit()
    except Error as e:
        logging.error("Error: %s" % e)


def get_emps_count():
    try:
        with conn:
            cursor.execute("SELECT * FROM employees")
            return len(cursor.fetchall())
    except Error as e:
        logging.error("Error: %s" % e)


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name("Doe")
print(emps)

update_pay(emp_1, 100000)
logging.info(f"Updated pay of employee {emp_1.fullname} is {emp_1.pay}")

remove_emp(emp_2)
count = get_emps_count()
logging.info(f"Employees count after delete {count}")

emps = get_emps_by_name("Doe")
print(emps)

