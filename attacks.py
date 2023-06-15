from utils.attack_entropy import entropy_elsewhere_during, entropy_for_timestamps

# LDAP
print(entropy_elsewhere_during('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0', 'Source IP'))
print(entropy_elsewhere_during('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0', 'Destination IP'))
print(entropy_for_timestamps('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0'))
