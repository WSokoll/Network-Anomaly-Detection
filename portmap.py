from datetime import datetime
from os.path import join

from utils.csv_reader import read_csv


# path to the 03-11 folder
from utils.entropy import calculate_entropy

FOLDER_PATH = r"C:\Users\wlade\Downloads\CSV-03-11\03-11"


def portmap():
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    header, rows, column_map = read_csv(join(FOLDER_PATH, 'Portmap.csv'))

    before_date = datetime.strptime('2018-11-03 09:43:00.0', time_format)
    after_date = datetime.strptime('2018-11-03 09:51:00.0', time_format)

    before = []
    during = []

    for row in rows:
        t = datetime.strptime(row[column_map['Timestamp']], time_format)

        # Get data before attack (before 9:43)
        if t < before_date:
            before.append(row)

        # Get data during attack (9:43 - 9:51)
        elif t < after_date:
            during.append(row)

    print('Source IP')
    print(calculate_entropy([d[column_map['Source IP']] for d in before]))
    print(calculate_entropy([d[column_map['Source IP']] for d in during]))

    print('Timestamp')
    print(calculate_entropy([d[column_map['Timestamp']] for d in before]))
    print(calculate_entropy([d[column_map['Timestamp']] for d in during]))

portmap()
