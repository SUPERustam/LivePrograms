import matplotlib.pyplot as plt
from datetime import datetime
from numpy import array, arange


def main():
    right_date = (datetime.today() - datetime(2020, 6, 24)).days + 2
    f = open('statistic.txt')
    f_new = [list(map(lambda z: int(float(z)), i)) for i in list(map(lambda x: x.strip().split(),
                                                                     list(map(lambda y: y, f))))[:2]]

    x = arange(1, right_date)
    x_speed = arange(6, right_date)
    y = array(f_new[0][:-1] + [0] * (len(x) - len(f_new[0])) + [f_new[0][-1]])  # add to result array
    y_speed = array(
        f_new[1][:-1] + [0] * (len(x_speed) - len(f_new[1])) + [f_new[1][-1]])  # add to speedreading array

    fig, ax = plt.subplots(nrows=1, ncols=2)

    ax[0].plot(x, y, "b", label="my results")
    ax[0].plot(x, array([20] * len(x)), 'r--', label="low standard of results")
    ax[0].plot(x, array([30] * len(x)), color='grey', linestyle="-.", label="normal results")
    ax[0].set_xlabel('days')
    ax[0].set_ylabel('pages')
    ax[0].set_title('results')
    ax[0].legend(loc=9)

    ax[1].plot(x_speed, y_speed, color="#FFF91A", label="my speedreading")
    ax[1].plot(x_speed, array([20] * len(x_speed)), 'r--', label="low standard of results")
    ax[1].plot(x_speed, array([30] * len(x_speed)), color='grey', linestyle="-.", label="normal speedreading")
    ax[1].set_xlabel('days')
    ax[1].set_ylabel('pages/hour')
    ax[1].set_title('speedreading')
    ax[1].legend(loc=9)

    # mytime = list(map(lambda item: item[0] / item[1], zip(list(y[5:]), list(y_speed))))
    # print(sum(mytime))
    # print(sum(mytime) / len(y_speed))
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # RuntimeWarning: invalid value encountered in double_scalars
    # mytime = list(map(lambda item: item[0] / item[1], zip(list(y[5:]), list(y_speed))))

    f = open('statistic.txt', 'w')
    a = " ".join(list(map(lambda z: str(z), y)))
    b = " ".join(list(map(lambda z: str(z), y_speed)))
    f.write(
        f"{a}\n{b}\nMiddle pages: {sum(y) / len(y)}; Sum pages: {sum(y)}; Max pages: {max(y)}\n"
        f"Middle speed: {sum(y_speed) / len(y_speed)}; Max speed: {max(y_speed)}")
    f.close()
    fig.tight_layout()
    plt.savefig("result.png")
    plt.show()


if __name__ == "__main__":
    main()
# TODO: integration with Telegram
