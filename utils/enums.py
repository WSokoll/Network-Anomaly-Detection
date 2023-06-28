# Uncomment the attack you want to analyze, and the parameters you want to calculate


FOLDER_PATH_03_11 = r"03-11"
FOLDER_PATH_01_12 = r"01-12"
RESULTS_01_12_PATH = r"01-12_RESULTS"
RESULTS_03_11_PATH = r"03-11_RESULTS"

ATTTACKS_03_11 = {
    # 'Portmap': ('2018-11-03 09:43:00.0', '2018-11-03 09:51:00.0'),
    # 'NetBIOS': ('2018-11-03 10:00:00.0', '2018-11-03 10:09:00.0'),
    # 'LDAP': ('2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0'),
    # 'MSSQL': ('2018-11-03 10:33:00.0', '2018-11-03 10:42:00.0'),
    # 'UDP': ('2018-11-03 10:53:00.0', '2018-11-03 11:03:00.0'),
    # 'UDPLag': ('2018-11-03 11:14:00.0', '2018-11-03 11:24:00.0'),
    # 'Syn': ('2018-11-03 11:28:00.0', '2018-11-03 17:35:00.0')
}

ATTTACKS_01_12 = {
    # 'DrDoS_NTP': ('2018-12-01 10:35:00.0', '2018-12-01 10:45:00.0'),
    # 'DrDoS_DNS': ('2018-12-01 10:52:00.0', '2018-12-01 11:05:00.0'),
    'DrDoS_LDAP': ('2018-12-01 11:22:00.0', '2018-12-01 11:32:00.0'),
    # 'DrDos_MSSQL': ('2018-12-01 11:36:00.0', '2018-12-01 11:45:00.0'),
    # 'DrDoS_NetBIOS': ('2018-12-01 11:50:00.0', '2018-12-01 12:00:00.0'),
    # 'DrDoS_SNMP': ('2018-12-01 12:12:00.0', '2018-12-01 12:23:00.0'),
    # 'DrDoS_SSDP': ('2018-12-01 12:27:00.0', '2018-12-01 12:37:00.0'),
    # 'DrDoS_UDP': ('2018-12-01 12:45:00.0', '2018-12-01 13:09:00.0'),
    # 'UDPLag': ('2018-12-01 13:11:00.0', '2018-12-01 13:15:00.0'),
    # 'Syn': ('2018-12-01 13:29:00.0', '2018-12-01 13:34:00.0'),
    # 'TFTP': ('2018-12-01 13:35:00.0', '2018-12-01 17:15:00.0'),
}



FEATURES = [' Source IP',
            ' Source Port',
            ' Destination IP',
            ' Destination Port',
            ' Protocol',
            ' Timestamp',
            ' Flow Duration',
            ' Total Fwd Packets',
            ' Total Backward Packets',
            'Total Length of Fwd Packets',
            ' Total Length of Bwd Packets',
            ' Fwd Packet Length Max',
            ' Fwd Packet Length Min',
            ' Fwd Packet Length Mean',
            ' Fwd Packet Length Std',
            'Bwd Packet Length Max',
            ' Bwd Packet Length Min',
            ' Bwd Packet Length Mean',
            ' Bwd Packet Length Std',
            'Flow Bytes/s',
            ' Flow Packets/s',
            ' Flow IAT Mean',
            ' Flow IAT Std',
            ' Flow IAT Max',
            ' Flow IAT Min',
            'Fwd IAT Total',
            ' Fwd IAT Mean',
            ' Fwd IAT Std',
            ' Fwd IAT Max',
            ' Fwd IAT Min',
            'Bwd IAT Total',
            ' Bwd IAT Mean',
            ' Bwd IAT Std',
            ' Bwd IAT Max',
            ' Bwd IAT Min',
            'Fwd PSH Flags',
            ' Bwd PSH Flags',
            ' Fwd URG Flags',
            ' Bwd URG Flags',
            ' Fwd Header Length',
            ' Bwd Header Length',
            'Fwd Packets/s',
            ' Bwd Packets/s',
            ' Min Packet Length',
            ' Max Packet Length',
            ' Packet Length Mean',
            ' Packet Length Std',
            ' Packet Length Variance',
            'FIN Flag Count',
            ' SYN Flag Count',
            ' RST Flag Count',
            ' PSH Flag Count',
            ' ACK Flag Count',
            ' URG Flag Count',
            ' CWE Flag Count',
            ' ECE Flag Count',
            ' Down/Up Ratio',
            ' Average Packet Size',
            ' Avg Fwd Segment Size',
            ' Avg Bwd Segment Size',
            ' Fwd Header Length.1',
            'Fwd Avg Bytes/Bulk',
            ' Fwd Avg Packets/Bulk',
            ' Fwd Avg Bulk Rate',
            ' Bwd Avg Bytes/Bulk',
            ' Bwd Avg Packets/Bulk',
            'Bwd Avg Bulk Rate',
            'Subflow Fwd Packets',
            ' Subflow Fwd Bytes',
            ' Subflow Bwd Packets',
            ' Subflow Bwd Bytes',
            'Init_Win_bytes_forward',
            ' Init_Win_bytes_backward',
            ' act_data_pkt_fwd',
            ' min_seg_size_forward',
            'Active Mean',
            ' Active Std',
            ' Active Max',
            ' Active Min',
            'Idle Mean',
            ' Idle Std',
            ' Idle Max',
            ' Idle Min',
            'SimillarHTTP',
            ' Inbound',
            ' Label']
