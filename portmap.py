from os.path import join

from utils.csv_reader import read_csv


# path to the 03-11 folder
FOLDER_PATH = r"path/to/the/folder/03-11"


def portmap():
    header, rows, column_map = read_csv(join(FOLDER_PATH, 'Portmap.csv'))

    print(header)

    for row in rows:
        print(row[column_map['Timestamp']])


portmap()
