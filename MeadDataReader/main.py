from Modules.data_reading import SignalBuilder
from matplotlib import pyplot as plt

signal = SignalBuilder("SignalExample.txt")
signal.ReadFromFile()

x_variable="time"
y_variable="gravity"

x_data, y_data = signal.generate_array(dimx=x_variable, dimy=y_variable)

plt.plot(x_data, y_data, color="red", marker=".")
plt.xlabel(x_variable)
plt.ylabel(y_variable)
plt.show()

print(x_data)
print(y_data)