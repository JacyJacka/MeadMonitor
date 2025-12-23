class SignalBuilder:

    def __init__(self, filename=""):
        self.__signal_time = []
        self.__signal_gravity = []
        self.__signal_temperature = []
        self.__filename = filename

    def ReadFromFile(self):
        with open(self.__filename) as f:
            for elem in f:
                time, gravity, temperature = elem.split()
                self.__signal_time.append(float(time))
                self.__signal_gravity.append(float(gravity))
                self.__signal_temperature.append(float(temperature))

    @property
    def signal_time(self):
        return self.__signal_time

    @property
    def signal_temperature(self):
        return self.__signal_temperature

    @property
    def signal_gravity(self):
        return self.__signal_gravity

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, name_file):
        self.__filename = name_file

    @property
    def __str__(self):
        str = f"<filename={self.__filename}"
        for i in range(len(self.__signal_time)):
            str += f"\n  time:{self.__signal_time[i]} \t gravity:{self.__signal_gravity[i]} \t temperature:{self.__signal_temperature[i]}"
        return str

    @property
    def __repr__(self):
        repr = f"<filename={self.__filename}"
        for i in range(len(self.__signal_time)):
            repr += f"\n  time:{self.__signal_time[i]} \t gravity:{self.__signal_gravity[i]} \t temperature:{self.__signal_temperature[i]}"
        return repr