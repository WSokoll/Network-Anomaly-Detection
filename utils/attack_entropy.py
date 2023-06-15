from datetime import datetime
from os.path import join

from utils.csv_reader import read_csv
from utils.entropy import calculate_entropy


def attack_entropies(folder_path, csv_file, _before_date, _after_date):

    time_format = '%Y-%m-%d %H:%M:%S.%f'
    header, rows, column_map = read_csv('{}\{}'.format(folder_path, csv_file))

    before_date = datetime.strptime(_before_date, time_format)
    after_date = datetime.strptime(_after_date, time_format)

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

