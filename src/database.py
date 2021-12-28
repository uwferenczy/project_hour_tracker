class Entry:
    def __init__(
            self,
            project,
            start_timestamp,
            finish_timestamp):
        self.project = project
        self.start_timestamp = start_timestamp
        self.finish_timestamp = finish_timestamp


def read_row_count():
    f = open("database.csv", "a+")
    counter = 0
    for line in f:
        print(counter)
        counter += 1
    f.close()
    return counter


def write_data(data):
    f = open("database.csv", "a")
    f.write(data)
    f.close()
    print("Data Saved Successfully!")


def import_data():
    f = open("database.csv", "r")
    data = []

    for row in f:

        data_split = row.split(",")
        entry = Entry(
            data_split[0],
            data_split[1],
            data_split[2]
        )
        data.append(entry)

    f.close()
    return data


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()