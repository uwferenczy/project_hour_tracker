import datetime
import os
import database
from texttable import Texttable
from datetime import date
from datetime import datetime
from datetime import timedelta

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


def print_hours(data):
    dataset = data
    #dataset.sort(key=lambda x: int(x.start_timestamp))
    t = Texttable(max_width=300)
    t.header(
        [
            "Project",
            "Start Time",
            "Finish Time"
        ]
    )

    for entry in dataset:
        t.add_row(
            [
                entry.project,
                entry.start_timestamp,
                entry.finish_timestamp.strip()
            ]
        )

    print(t.draw())

