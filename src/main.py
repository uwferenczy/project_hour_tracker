import database
import display

project_count = database.read_row_count()
print(f'You have {project_count} projects.')
display.menu()
display.track_hours()