from matplotlib import pyplot as plt
from scipy.optimize import curve_fit



linear_func = lambda x, m, q: m*x + q


def Plot_data_and_regresssion(x_data, y_data, XLABEL="", YLABEL="", plot_color="red", regression_size = 0, regression_color = "blue", regression_function = linear_func):
    plt.plot(x_data, y_data, color=plot_color)
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    popt, cov = 0, 0
    if regression_size != 0:
        size = len(x_data)
        x_fit = x_data[size - 5000:]
        y_fit = y_data[size - 5000:]
        popt, cov = curve_fit(regression_function, x_fit, y_fit)
        y_reg = [regression_function(elem, float((popt)[0]), float((popt)[1])) for elem in x_fit]
        plt.plot(x_fit, y_reg, color=regression_color)
    plt.show()

    return popt, cov
