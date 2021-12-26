import datetime
import os
import database

def menu():
    print(f'\nPlease pick an option:\n'
    f'1. Display Project Hours\n'
    f'2. Add new Project\n'
    f'3. Track Project Hours\n'
    f'4. Exit\n')


def track_hours():
    project_name = input('Which project do you want to track hours for? ')
    start_time = datetime.datetime.now()
    input('Press enter to stop recording time. ')
    stop_time = datetime.datetime.now()
    database.write_data(f'{project_name},{start_time},{stop_time}')
    return f'{project_name},{start_time},{stop_time}'

