class SignalBuilder:

    def __init__(self, filename=""):
        self._signal_time = []
        self._signal_gravity = []
        self._signal_temperature = []
        self._filename = filename

    def ReadFromFile(self):
        self._signal_time = []
        self._signal_gravity = []
        self._signal_temperature = []
        with open(self._filename) as f:
            for elem in f:
                time, gravity, temperature = elem.split()
                self._signal_time.append(float(time))
                self._signal_gravity.append(float(gravity))
                self._signal_temperature.append(float(temperature))

    @property
    def signal_time(self):
        return self._signal_time

    @property
    def signal_temperature(self):
        return self._signal_temperature

    @property
    def signal_gravity(self):
        return self._signal_gravity

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, name_file):
        self._filename = name_file

    def __str__(self):
        result = f"<filename={self._filename}"
        for i in range(len(self._signal_time)):
            result += f"\n  time:{self._signal_time[i]} \t gravity:{self._signal_gravity[i]} \t temperature:{self._signal_temperature[i]}"
        return result

    def __repr__(self):
        result = f"<filename={self._filename}"
        for i in range(len(self._signal_time)):
            result += f"\n  time:{self._signal_time[i]} \t gravity:{self._signal_gravity[i]} \t temperature:{self._signal_temperature[i]}"
        return result
