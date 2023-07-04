from utils.csv_reader import append_to_file_before_timestamp, read_single_column
import csv
import json

from utils.entropy import calculate_entropy

FOLDER_PATH_03_11 = r"..\\03-11"
ATTTACKS_03_11 = {
    'Portmap': ('2018-11-03 09:43:00.0', '2018-11-03 09:51:00.0'),
    'NetBIOS': ('2018-11-03 10:00:00.0', '2018-11-03 10:09:00.0'),
    'LDAP': ('2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0'),
    'MSSQL': ('2018-11-03 10:33:00.0', '2018-11-03 10:42:00.0'),
    'UDP': ('2018-11-03 10:53:00.0', '2018-11-03 11:03:00.0'),
    'UDPLag': ('2018-11-03 11:14:00.0', '2018-11-03 11:24:00.0'),
    'Syn': ('2018-11-03 11:28:00.0', '2018-11-03 17:35:00.0')
}

FOLDER_PATH_01_12 = r"..\\01-12"
ATTTACKS_01_12 = {
    'DrDoS_NTP': ('2018-12-01 10:35:00.0', '2018-12-01 10:45:00.0'),
    'DrDoS_DNS': ('2018-12-01 10:52:00.0', '2018-12-01 11:05:00.0'),
    'DrDoS_LDAP': ('2018-12-01 11:22:00.0', '2018-12-01 11:32:00.0'),
    'DrDos_MSSQL': ('2018-12-01 11:36:00.0', '2018-12-01 11:45:00.0'),
    'DrDoS_NetBIOS': ('2018-12-01 11:50:00.0', '2018-12-01 12:00:00.0'),
    'DrDoS_SNMP': ('2018-12-01 12:12:00.0', '2018-12-01 12:23:00.0'),
    'DrDoS_SSDP': ('2018-12-01 12:27:00.0', '2018-12-01 12:37:00.0'),
    'DrDoS_UDP': ('2018-12-01 12:45:00.0', '2018-12-01 13:09:00.0'),
    'UDPLag': ('2018-12-01 13:11:00.0', '2018-12-01 13:15:00.0'),
    'Syn': ('2018-12-01 13:29:00.0', '2018-12-01 13:34:00.0'),
    'TFTP': ('2018-12-01 13:35:00.0', '2018-12-01 17:15:00.0'),
}


# Get entropy for all parameters from all files before the attacks
def generate_file_of_entries_before_attacks():
    outside_of_attacks_file_path = '../no_attack.csv'

    for day in [1, 2]:
        if day == 1:
            attack_list = ATTTACKS_03_11
            input_file_path = FOLDER_PATH_03_11 + "\\"
        else:
            attack_list = ATTTACKS_01_12
            input_file_path = FOLDER_PATH_01_12 + "\\"

        for attack_name, timestamps in attack_list.items():
            timestamp_start = timestamps[0]
            input_file = input_file_path + attack_name + '.csv'

            append_to_file_before_timestamp(input_file, timestamp_start, outside_of_attacks_file_path)
            print(input_file)

def calculate_base_entropy():
    with open('..\\03-11\\LDAP.csv', newline='\n') as f:
        reader = csv.reader(f)
        first_row = next(reader)
        features = [feature for feature in first_row]
        # First two parameters are Unnamed: 0, whatever it is and Flow ID so we don't need to calculate their entropy
        features.pop(0)
        features.pop(0)

    with open('..\\base_entropy.json', mode='a', newline='\n') as base_entropy_file:
        entries = {}
        for feature in features:
            rows = read_single_column('../no_attack.csv', feature)
            print(feature)
            entries[feature] = calculate_entropy(rows)
        base_entropy_file.write(json.dumps(entries) + "\n")


