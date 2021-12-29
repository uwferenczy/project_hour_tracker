import database
import display
import backend

while True:
    selection = display.menu()
    if selection == '1':
        print('Display Project Hours')
    if selection == '2':
        backend.add_new_project()
    if selection == '3':
        backend.track_project_hours()
    if selection == '4':
        print('Thank you for using this application')
        quit()