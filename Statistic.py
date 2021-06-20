import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots()  # ax - axes or array of axes
    y = np.array([1, 1, 1, 3, 1, 1, 1, 2, 2, 2, 2, 0, 1, 0, 2, 3, 2, 2, 3])
    x = np.array(range(1, len(y) + 1))
    schedule_y = np.array([2, 3])
    schedule_x = np.array([15, 16])

    ax.plot(x, y, label='figure of tasks performance')
    ax.scatter(schedule_x, schedule_y, color='red', marker='P', label='days, when i use schedule')
    ax.set_title("Tasks performance")
    ax.set_ylabel('Done tasks')
    ax.set_xlabel('Days, first day == 2 June')
    ax.legend()

    fig.show()
    fig.savefig('Statistic_image.jpg')


if __name__ == '__main__':
    main()

