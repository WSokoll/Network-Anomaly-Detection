from datetime import datetime
from os.path import join

from utils.csv_reader import read_csv
from utils.entropy import calculate_entropy

FOLDER_PATH = r"F:\studia\6 sem\KiK\CSV-03-11\03-11"


def udp():
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    header, rows, column_map = read_csv(join(FOLDER_PATH, 'UDP.csv'))

    before_date = datetime.strptime('2018-11-03 10:53:00.0', time_format)
    after_date = datetime.strptime('2018-11-03 11:03:00.0', time_format)

    elsewhere = []
    during = []

    for row in rows:
        t = datetime.strptime(row[column_map['Timestamp']], time_format)


        # Get data during attack
        if before_date <= t <= after_date:
            during.append(row)
        # Get data before attack
        else:
            elsewhere.append(row)

    print('Source IP')
    print(calculate_entropy([d[column_map['Source IP']] for d in elsewhere]))
    print(calculate_entropy([d[column_map['Source IP']] for d in during]))

    print('Destination IP')
    print(calculate_entropy([d[column_map['Destination IP']] for d in elsewhere]))
    print(calculate_entropy([d[column_map['Destination IP']] for d in during]))

    print('Timestamp')
    print(calculate_entropy([d[column_map['Timestamp']] for d in elsewhere]))
    print(calculate_entropy([d[column_map['Timestamp']] for d in during]))

udp()
