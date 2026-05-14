import unittest
from MeadDataReader.Modules.data_reading import SignalBuilder


class SignalBuilderTests(unittest.TestCase):

    def test_default_state(self):
        builder = SignalBuilder()
        self.assertEqual(builder.filename, "")
        self.assertEqual(builder.signal_time, [])
        self.assertEqual(builder.signal_gravity, [])
        self.assertEqual(builder.signal_temperature, [])

    def test_filename_in_constructor(self):
        builder = SignalBuilder("somefile.txt")
        self.assertEqual(builder.filename, "somefile.txt")

    def test_filename_setter(self):
        builder = SignalBuilder()
        builder.filename = "newfile.txt"
        self.assertEqual(builder.filename, "newfile.txt")

    def test_read_file(self):
        builder = SignalBuilder("MeadDataReader/tests/file_test.txt")
        builder.ReadFromFile()
        self.assertEqual(builder.signal_time, [1.0, 4.0, 7.0])
        self.assertEqual(builder.signal_gravity, [2.0, 5.0, 8.0])
        self.assertEqual(builder.signal_temperature, [3.0, 6.0, 9.0])

    def test_read_file_twice_does_not_duplicate(self):
        builder = SignalBuilder("MeadDataReader/tests/file_test.txt")
        builder.ReadFromFile()
        builder.ReadFromFile()
        self.assertEqual(len(builder.signal_time), 3)
        self.assertEqual(len(builder.signal_gravity), 3)
        self.assertEqual(len(builder.signal_temperature), 3)

    def test_read_nonexistent_file_raises(self):
        builder = SignalBuilder("nonexistent_file.txt")
        with self.assertRaises(FileNotFoundError):
            builder.ReadFromFile()

    def test_read_empty_file(self):
        builder = SignalBuilder("MeadDataReader/tests/empty_test.txt")
        builder.ReadFromFile()
        self.assertEqual(builder.signal_time, [])
        self.assertEqual(builder.signal_gravity, [])
        self.assertEqual(builder.signal_temperature, [])

    def test_str_representation(self):
        builder = SignalBuilder("test.txt")
        self.assertIn("test.txt", str(builder))

    def test_repr_representation(self):
        builder = SignalBuilder("test.txt")
        self.assertIn("test.txt", repr(builder))


if __name__ == '__main__':
    unittest.main()
