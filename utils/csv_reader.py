import csv


def read_csv(filepath):
    file = open(filepath)
    reader = csv.reader(file)

    headers = next(reader)
    rows = [row for row in reader]

    # create map to improve data access
    column_map = {header.lstrip(): position for position, header in enumerate(headers)}

    return headers, rows, column_map
