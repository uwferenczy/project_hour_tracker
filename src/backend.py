import sqlite3
import datetime
from datetime import datetime


def create_new_tables():
    conn = sqlite3.connect('projectTracker.db')
    c = conn.cursor()

    c.execute("""
    CREATE TABLE projects (
        project_id INTEGER,
        project_name TEXT,
        create_date TEXT
    )
    
    CREATE TABLE hours (
        project_id INTEGER,
        start_ts TEXT,
        finish_ts TEXT
    )
    """)

    conn.commit()
    conn.close()


def get_projects():
    conn = sqlite3.connect('projectTracker.db')
    c = conn.cursor()

    c.execute("""SELECT * FROM projects""")
    data = c.fetchall()
    conn.commit()
    conn.close()
    return data


def add_new_project():
    id = len(get_projects())+1
    conn = sqlite3.connect('projectTracker.db')
    c = conn.cursor()
    name = input("What is the name of the project you want to add? ")
    create_date = datetime.now()
    c.execute("INSERT INTO projects VALUES (?,?,?)", (id, name, create_date))
    conn.commit()
    conn.close()


def track_project_hours():
    data = get_projects()
    conn = sqlite3.connect('projectTracker.db')
    c = conn.cursor()
    print('Select a project from the list below:\n')
    for row in data:
        print(f'{row[0]} - {row[1]}')
    selection = input()
    start_time = datetime.now()
    input('Press Enter to stop tracking project hours')
    end_time = datetime.now()
    c.execute("INSERT INTO hours VALUES (?,?,?)", (int(selection), start_time, end_time))
    conn.commit()
    conn.close()
