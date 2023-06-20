from utils.attack_entropy import entropy_elsewhere_during, entropy_for_timestamps
from utils.chart import draw_bar_chart
import matplotlib.pyplot as plt

# LDA
source_ip_entropy = entropy_elsewhere_during('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0', 'Source IP')
destination_ip_entropy = entropy_elsewhere_during('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0', 'Destination IP')
timestamps_entropy = entropy_for_timestamps('LDAP.csv', '2018-11-03 10:21:00.0', '2018-11-03 10:30:00.0')

# print results
print(source_ip_entropy)
print(destination_ip_entropy)
print(timestamps_entropy)

# draw charts
draw_bar_chart(source_ip_entropy)
draw_bar_chart(destination_ip_entropy)
draw_bar_chart(timestamps_entropy)

plt.show()
