import csv
import pandas as pd


def read_csv(filepath):
    file = open(filepath)
    reader = csv.reader(file)

    headers = [h.strip() for h in next(reader)]
    rows = [row for row in reader]

    # create map to improve data access
    column_map = {header.lstrip(): position for position, header in enumerate(headers)}

    return headers, rows, column_map


def read_single_column(filepath, column_name):
    file = pd.read_csv(filepath, low_memory=False)
    return file[' ' + column_name.strip()].tolist()
