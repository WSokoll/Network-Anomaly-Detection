import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

from datetime import datetime, timedelta
from os.path import join
from utils.csv_reader import read_single_column
from utils.entropy import calculate_entropy

FOLDER_PATH = r"path\to\folder"


def entropy_elsewhere_during(csv_file, _before_date, _after_date, parameter):
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    rows = read_single_column(join(FOLDER_PATH, csv_file), parameter)
    timestamps = read_single_column(join(FOLDER_PATH, csv_file), 'Timestamp')

    before_date = datetime.strptime(_before_date, time_format)
    after_date = datetime.strptime(_after_date, time_format)

    elsewhere = []
    during = []

    # data for chart
    sample = []
    sample_time = []
    sample_entropy = []
    time = 0

    for i in range(len(rows)):
        t = datetime.strptime(timestamps[i], time_format)

        # Get data during attack
        if before_date <= t <= after_date:
            during.append(rows[i])
        # Get data before attack
        else:
            elsewhere.append(rows[i])

        # entropy calculation for samples
        if i == 0:
            time = t
        else:
            if t >= (time + timedelta(seconds=10)):
                time = t
                sample_entropy.append(calculate_entropy(sample))
                sample_time.append(time)

        sample.append(rows[i])

    # draw chart
    plt.figure()
    plt.title(parameter)
    plt.ylabel('Entropy')
    plt.plot(sample_time, sample_entropy, color='green', linestyle='dashed', linewidth=2,
             marker='o', markerfacecolor='red', markersize=5)

    return {
        'parameter': parameter,
        'elsewhere': calculate_entropy(elsewhere),
        'during': calculate_entropy(during)
    }


def entropy_for_timestamps(csv_file, _before_date, _after_date):
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    timestamps = read_single_column(join(FOLDER_PATH, csv_file), 'Timestamp')

    before_date = datetime.strptime(_before_date, time_format)
    after_date = datetime.strptime(_after_date, time_format)

    elsewhere = []
    during = []

    for t in timestamps:
        t = datetime.strptime(t, time_format)

        # Get data during attack
        if before_date <= t <= after_date:
            during.append(t)
        # Get data before attack
        else:
            elsewhere.append(t)

    elsewhere_gaps = []
    during_gaps = []

    for i in range(len(elsewhere) - 1):
        elsewhere_gaps.append((elsewhere[i + 1] - elsewhere[i]).total_seconds())

    for i in range(len(during) - 1):
        during_gaps.append((during[i + 1] - during[i]).total_seconds())

    return {
        'parameter': 'Timestamp gaps',
        'elsewhere': calculate_entropy(elsewhere_gaps),
        'during': calculate_entropy(during_gaps)
    }
