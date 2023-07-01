import csv
from datetime import datetime
import json
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

    # Some parameters don't have a leading space and others do, so we need to adjust those columns
    if column_name in ['Unnamed: 0', 'Bwd Packet Length Max' , 'Flow ID', 'Total Length of Fwd Packets', 'Flow Bytes/s',
                       'Fwd IAT Total', 'Bwd IAT Total', 'Fwd PSH Flags', 'Fwd Packets/s', 'FIN Flag Count',
                       'Fwd Avg Bytes/Bulk', 'Bwd Avg Bulk Rate', 'Subflow Fwd Packets', 'Init_Win_bytes_backward',
                       'Active Mean', 'Idle Mean', 'SimillarHTTP', 'Init_Win_bytes_forward']:
        return file[column_name.strip()].tolist()
    else:
        return file[' ' + column_name.strip()].tolist()


def append_to_file_before_timestamp(csv_file, _before_date, path_to_save):
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    file = open(csv_file)
    reader = csv.reader(file)
    timestamps = read_single_column(csv_file, 'Timestamp')
    # To omit the headers
    row = next(reader)
    before_date = datetime.strptime(_before_date, time_format)
    with open(path_to_save, "a") as output_file:
        for timestamp in timestamps:
            t = datetime.strptime(timestamp, time_format)
            # Get data during attack
            if t <= before_date:
                row = next(reader)
                output_file.write(json.dumps(row) + "\n")
            else:
                file.close()
                output_file.close()
                return

