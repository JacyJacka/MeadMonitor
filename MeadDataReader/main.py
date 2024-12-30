from Modules.data_reading import SignalBuilder
from matplotlib import pyplot as plt

signal = SignalBuilder("SignalExample.txt")
signal.ReadFromFile()

XLABEL="time"
YLABEL="gravity"

x_data, y_data = signal.generate_array(dimx=XLABEL, dimy=YLABEL)

plt.plot(x_data, y_data, color="red")
plt.xlabel(XLABEL)
plt.ylabel(YLABEL)
plt.show()
