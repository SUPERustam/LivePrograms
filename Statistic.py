import matplotlib.pyplot as plt
import numpy as np


def main():
    y = np.array([1, 1, 1, 3, 1, 1, 1, 2, 2, 2, 2, 0, 1])
    x = np.array(range(1, len(y) + 1))

    plt.plot(x, y)
    plt.ylabel('Done tasks')
    plt.xlabel('Days, first day == 2 June')
    plt.show()


if __name__ == '__main__':
    main()
