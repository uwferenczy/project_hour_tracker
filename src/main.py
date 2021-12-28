import database
import display

data = database.import_data()
display.track_hours()
display.print_hours(data)