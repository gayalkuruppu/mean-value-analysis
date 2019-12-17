import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def exponential_fit(x, a, b, c):
    return a*np.exp(-b*x) + c


if __name__ == "__main__":
    x = np.array([521, 7919, 10007, 100003, 1000003, 10000019])
    y = np.array([26071.88497, 9762.025802, 7819.574098, 954.8169493, 97.67334488, 10.94243415])
    fitting_parameters, covariance = curve_fit(exponential_fit, x, y)
    a, b, c = fitting_parameters

    next_x = 251
    next_y = exponential_fit(next_x, a, b, c)

    plt.plot(y)
    plt.plot(np.append(y, next_y), 'ro')
    plt.show()
