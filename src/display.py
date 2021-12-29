import datetime
import os
import database
from texttable import Texttable
from datetime import date
from datetime import datetime
from datetime import timedelta


def menu():
    return input(f'\nPlease pick an option:\n'
    f'1. Display Project Hours\n'
    f'2. Add New Project\n'
    f'3. Track Project Hours\n'
    f'4. Exit\n')


def dateparser(date):
    paresed_date = []
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = int(date[11:13])
    second = int(date[14:16])
    paresed_date.append(year)
    paresed_date.append(month)
    paresed_date.append(day)
    paresed_date.append(hour)
    paresed_date.append(second)
    return(paresed_date)



def track_hours():
    project_name = input('Which project do you want to track hours for? ')
    start_time = datetime.now()
    input('Press enter to stop recording time. ')
    stop_time = datetime.now()
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
            "Finish Time",
            "Test"
        ]
    )

    for entry in dataset:
        test = datetime.fromisoformat(entry.start_timestamp.strip())
        t.add_row(
            [
                entry.project,
                entry.start_timestamp.strip(),
                entry.finish_timestamp.strip(),
                f'{(dateparser(entry.finish_timestamp.strip())[3] - dateparser(entry.start_timestamp.strip())[3])+round((dateparser(entry.finish_timestamp.strip())[4]-dateparser(entry.start_timestamp.strip())[4])/60,2)}'
            ]
        )

    print(t.draw())

