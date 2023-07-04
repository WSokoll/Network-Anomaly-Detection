from datetime import datetime

import pandas as pd

from utils.attack_entropy import entropy_elsewhere_during, entropy_for_timestamps
from utils.chart import draw_bar_chart
import matplotlib.pyplot as plt
import csv
import json
import os, shutil
from utils.enums import FOLDER_PATH_01_12, FOLDER_PATH_03_11, RESULTS_03_11_PATH, RESULTS_01_12_PATH, ATTTACKS_01_12, ATTTACKS_03_11, FEATURES

# Read about radviz charts

# A promising article about cumulative entropy in ddos detection - maybe we should try it
# https://link.springer.com/chapter/10.1007/978-3-540-77048-0_35


for day in [1, 2]:
    if day == 1:
        attack_list = ATTTACKS_03_11
        input_file_path = FOLDER_PATH_03_11 + "\\"
    else:
        attack_list = ATTTACKS_01_12
        input_file_path = FOLDER_PATH_01_12 + "\\"

    for attack_name, timestamps in attack_list.items():
        timestamp_start = timestamps[0]
        timestamp_end = timestamps[1]

        if day == 1:
            results_file_path = RESULTS_03_11_PATH + "\\" + attack_name
            entropy_output_file_path = RESULTS_03_11_PATH + "\\" + attack_name + "\\" + attack_name + ".txt"
        else:
            results_file_path = RESULTS_01_12_PATH + "\\" + attack_name
            entropy_output_file_path = RESULTS_01_12_PATH + "\\" + attack_name + "\\" + attack_name + ".txt"

        input_file = input_file_path + attack_name + '.csv'
        if not os.path.exists(results_file_path):
            os.makedirs(results_file_path)

        for filename in os.listdir(results_file_path):
            file_path = os.path.join(results_file_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


        with open(entropy_output_file_path, "a") as output_file:
            for feature in FEATURES:
                chart_path = results_file_path + "\\" + feature.replace(" ", "").replace('/', '') + ".png"
                if feature == 'Timestamp':
                    entropy = entropy_for_timestamps(input_file, timestamp_start, timestamp_end, chart_path)
                else:
                    entropy = entropy_elsewhere_during(input_file, timestamp_start, timestamp_end, feature, chart_path)
                print(entropy)
                output_file.write(json.dumps(entropy) + "\n")


#
#####
# LDA
# source_ip_entropy = entropy_elsewhere_during('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0', 'Source IP')
# destination_ip_entropy = entropy_elsewhere_during('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0', 'Destination IP')
# timestamps_entropy = entropy_for_timestamps('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0')
#
#
#
# # print results
# print(source_ip_entropy)
# print(destination_ip_entropy)
# print(timestamps_entropy)
#
# draw_bar_chart(source_ip_entropy)
# draw_bar_chart(destination_ip_entropy)
# draw_bar_chart(timestamps_entropy)
#
# plt.show()
