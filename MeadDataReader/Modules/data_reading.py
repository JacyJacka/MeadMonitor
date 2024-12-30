from matplotlib import pyplot as plt

class point:

    def __init__(self, list = []):
        try:
            if len(list)!=0:
                time, gravity, temperature = list
                self.__time = float(time)
                self.__gravity = float(gravity)
                self.__temperature = float(temperature)
            else:
                self.__time = 0.
                self.__gravity = 0.
                self.__temperature = 0.
        except ValueError:
            print(f"ERROR: Invalid value read in file: input =[{list}]")
            self.__time = 0.
            self.__gravity = 0.
            self.__temperature = 0.

    @property
    def time(self):
        return self.__time

    # @time.setter
    # def time(self, time):
    #     self.__time = time

    @property
    def gravity(self):
        return self.__gravity

    # @gravity.setter
    # def gravity(self, gravity):
    #     self.__gravity = gravity

    @property
    def temperature(self):
        return self.__temperature

    # @temperature.setter
    # def temperature(self, temperature):
    #     self.__temperature = temperature

    def __eq__(self, other):
        return self.__time == other.time and self.__gravity == other.gravity and self.__temperature == other.temperature

    def __ne__(self, other):
        return self.__time != other.time or self.__gravity != other.gravity or self.__temperature != other.temperature

    def __str__(self):
        return f"<time={self.__time}, gravity={self.__gravity}, temperature={self.__temperature}>"

    def __repr__(self):
        return f"<time={self.__time}, gravity={self.__gravity}, temperature={self.__temperature}>"

class SignalBuilder:

    def __init__(self, filename=""):
        self.__signal=[]
        self.__filename = filename

    def ReadFromFile(self):
        with open(self.__filename) as f:
            self.__signal = [point(elem.split()) for elem in f.readlines()]
        f.close()

    def select_data(self, data_type, point):
        if data_type == "time":
            return point.time
        elif data_type == "gravity":
            return point.gravity
        elif data_type == "temperature":
            return point.temperature
        else:
            return -1000.

    def generate_array(self, dimx="time", dimy="gravity"):
         x_data = []
         y_data = []
         for elem in self.__signal:
             x_data.append(self.select_data(dimx, elem))
             y_data.append(self.select_data(dimy, elem))
         return [x_data, y_data]

    @property
    def signal(self):
        return self.__signal

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, name_file):
        self.__filename = name_file

    def __str__(self):
        str = f"<filename={self.__filename}"
        for elem in self.__signal:
            str += f"\n  {elem}"
        return str

    def __repr__(self):
        repr = f"<filename={self.__filename}"
        for elem in self.__signal:
            repr += f"\n  {elem}\n"
        return repr