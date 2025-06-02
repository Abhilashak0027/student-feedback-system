import sqlite3

def connect():
    return sqlite3.connect('student_data.db')

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no INTEGER NOT NULL,
            subject TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_student(name, roll_no, subject, marks):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, roll_no, subject, marks) VALUES (?, ?, ?, ?)",
        (name, roll_no, subject, marks)
    )
    conn.commit()
    conn.close()

def get_all_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name, roll_no, subject, marks FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows
