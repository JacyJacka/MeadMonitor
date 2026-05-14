from matplotlib import pyplot as plt
from Modules.data_reading import SignalBuilder
from Modules.data_analysis import Plot_data_and_regression


signal = SignalBuilder("SignalExample.txt")
signal.ReadFromFile()

XLABEL = "time"
YLABEL = "gravity"
REGR_SIZE = 5000

x_data, y_data = signal.signal_time, signal.signal_gravity

f = lambda x, m, q: m*x + q
popt, cov = Plot_data_and_regression(x_data, y_data,
                                     xlabel=XLABEL, ylabel=YLABEL, plot_color="red",
                                     regression_size=REGR_SIZE, regression_color="blue",
                                     regression_function=f)

print("popt:",popt)
print ("cov:",cov)

