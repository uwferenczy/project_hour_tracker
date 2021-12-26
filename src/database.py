def read_row_count():
    f = open("database.csv", "a+")
    counter = 0
    for line in f:
        counter += 1
    f.close()
    return counter


def write_data(data):
    f = open("database.csv", "a")
    f.write(data)
    f.close()
    print("Data Saved Successfully!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()