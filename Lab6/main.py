# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt


def nump():
    x = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0,
                  1,
                  1,
                  0])

    x = 2*x-1
    # print(x)
    z = x[:, 0]*x[:, 1]


    z = np.sum(x, axis=1)
    z = z**2
    # print(z)

    # print(np.shape(x))
    # print(np.shape(y))

    # x_row_sum = x[0 ,:]+x[1 ,:]+x[2 ,:]+x[3 ,:]
    # print(x_row_sum)

    x = np.array([2001, 2002, 2003, 2004, 2005])
    y = np.array([1, 4, 9, 0.5, 25])
    plt.scatter(x, y, marker='x', color='black')

    y = 4 * x - 8004
    plt.plot(x, y, color='red')

    y = x**2 - 4000*x + 4000000
    plt.plot(x, y, color='green')

    plt.show()

    # plt.plot(x, y, color='blue')
    # plt.scatter(x, y, marker='x', color ='black', label = "Scatter")
    # plt.plot(x, y, color='blue', label = "Line")
    # plt.xlabel('Years')
    # plt.ylabel('Sales( in K$)')
    # plt.legend()
    # plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nump()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
