import matplotlib.pyplot as plt


def draw_bar_chart(data):
    # print(data)

    left = [1, 2]
    height = [data['elsewhere'], data['during']]
    label = ['elsewhere', 'during']

    plt.figure()
    plt.bar(left, height, tick_label=label, color=['green', 'red'])
    plt.ylabel('Entropy')
    plt.title(data['parameter'])



