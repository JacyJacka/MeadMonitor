from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


linear_func = lambda x, m, q: m*x + q


def Plot_data_and_regression(x_data, y_data, xlabel="", ylabel="", plot_color="red", regression_size=0, regression_color="blue", regression_function=linear_func):
    plt.plot(x_data, y_data, color=plot_color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    popt, cov = None, None
    if regression_size != 0:
        size = len(x_data)
        actual_size = min(regression_size, size)
        x_fit = x_data[size - actual_size:]
        y_fit = y_data[size - actual_size:]
        popt, cov = curve_fit(regression_function, x_fit, y_fit)
        y_reg = [regression_function(elem, float(popt[0]), float(popt[1])) for elem in x_fit]
        plt.plot(x_fit, y_reg, color=regression_color)
    plt.show()

    return popt, cov
