import unittest
from MeadDataReader.Modules.data_reading import *


class PointAndFileTests(unittest.TestCase):

    # def test_point_class(self):
    #     p = point()
    #     self.assertEqual(p.time, 0)
    #     self.assertEqual(p.temperature, 0)
    #     self.assertEqual(p.gravity, 0)
    #
    # def test_poit_parse(self):
    #     p = point(["a", "b", "c"])
    #     self.assertEqual(p.time, 0)
    #     self.assertEqual(p.temperature, 0)
    #     self.assertEqual(p.gravity, 0)
    #
    # def test_point_operators(self):
    #     p1 = point([1,2,3])
    #     p2 = point([1,2,3])
    #     self.assertEqual(p1, p2)
    #
    # def test_select_data(self):
    #     p1 = point([1,2,3])
    #     builder = SignalBuilder()
    #     self.assertEqual(p1.time, builder.select_data("time", p1))
    #     self.assertEqual(p1.gravity, builder.select_data("gravity", p1))
    #     self.assertEqual(p1.temperature, builder.select_data("temperature", p1))
    #     self.assertEqual(-1000, builder.select_data("pippo", p1))


    def test_read_file(self):
        filename = "MeadDataReader/tests/file_test.txt"
        ben_time = [1,4,7]
        ben_gravity = [2,5,8]
        ben_temperature = [3,6,9]
        data_holder = SignalBuilder()
        data_holder.filename = filename
        self.assertEqual(filename, data_holder.filename)
        data_holder.ReadFromFile()
        self.assertEqual(ben_time, data_holder.signal_time)
        self.assertEqual(ben_gravity, data_holder.signal_gravity)
        self.assertEqual(ben_temperature, data_holder.signal_temperature)

    #
    # def test_generate_array(self):
    #     filename = "MeadDataReader/tests/file_test.txt"
    #     ben_x = [1.0, 4.0]
    #     ben_y = [2.0, 5.0]
    #     data_holder = SignalBuilder()
    #     data_holder.filename = filename
    #     self.assertEqual(filename, data_holder.filename)
    #     data_holder.ReadFromFile()
    #     arr_x, arr_y =data_holder.generate_array("time", "gravity")
    #     for i in range(0, len(ben_x)):
    #         self.assertEqual(ben_x[i], arr_x[i])
    #     for i in range(0, len(ben_y)):
    #         self.assertEqual(ben_y[i], arr_y[i])


if __name__ == '__main__':
    unittest.main()
