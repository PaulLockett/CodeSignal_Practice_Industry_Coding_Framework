import unittest
from simulation import simulate_coding_framework


class TestSimulateCodingFramework(unittest.TestCase):

    def assert_simulation(self, test_data):
        """
        :param test_data: Pairs of command, expected_output. Each command is a list of strings ["commandname", "arg1", "arg2" ...]
        and each expected_output is the expected return value for that command
        """
        commands, expected_outputs = zip(*test_data)
        expected_outputs = list(expected_outputs)
        actual_outputs = simulate_coding_framework(commands)
        self.assertEqual(expected_outputs, actual_outputs, f"Failed for commands: {commands}")

    def test_group_1(self):
        test_data = [
            (["FILE_UPLOAD", "Cars.txt", "200kb"], None),
            (["FILE_GET", "Cars.txt"], "200kb"),
            (["FILE_COPY", "Cars.txt", "Cars2.txt"], None),
            (["FILE_GET", "Cars2.txt"], "200kb")
        ]
        self.assert_simulation(test_data)

    def test_group_2(self):
        test_data = [
            (["FILE_UPLOAD", "Foo.txt", "100kb"], None),
            (["FILE_UPLOAD", "Bar.csv", "200kb"], None),
            (["FILE_UPLOAD", "Baz.pdf", "300kb"], None),
            (["FILE_SEARCH", "Ba"], ["Baz.pdf", "Bar.csv"])
        ]
        self.assert_simulation(test_data)

    def test_group_3(self):
        test_data = [
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Python.txt", "150kb"], None),
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600], None),
            (["FILE_GET_AT", "2021-07-01T13:00:01", "Python.txt"], "150kb"),
            (["FILE_COPY_AT", "2021-07-01T12:00:00", "Python.txt", "PythonCopy.txt"], None),
            (["FILE_SEARCH_AT", "2021-07-01T12:00:00", "Py"], ["Python.txt", "PythonCopy.txt"]),
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Expired.txt", "100kb", 1], None),
            (["FILE_GET_AT", "2021-07-01T12:00:02", "Expired.txt"], None),
            (["FILE_COPY_AT", "2021-07-01T12:00:00", "CodeSignal.txt", "CodeSignalCopy.txt"], None),
            (["FILE_SEARCH_AT", "2021-07-01T12:00:00", "Code"], ["CodeSignal.txt", "CodeSignalCopy.txt"])
        ]

        self.assert_simulation(test_data)

    def test_group_4(self):
        test_data = [
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Initial.txt", "100kb"], None),
            (["FILE_UPLOAD_AT", "2021-07-01T12:05:00", "Update1.txt", "150kb", 3600], None),
            (["FILE_GET_AT", "2021-07-01T12:10:00", "Initial.txt"], "100kb"),
            (["FILE_COPY_AT", "2021-07-01T12:15:00", "Update1.txt", "Update1Copy.txt"], None),
            (["FILE_UPLOAD_AT", "2021-07-01T12:20:00", "Update2.txt", "200kb", 1800], None),
            (["ROLLBACK", "2021-07-01T12:10:00"], None),
            (["FILE_GET_AT", "2021-07-01T12:25:00", "Update1.txt"], None),
            (["FILE_GET_AT", "2021-07-01T12:25:00", "Initial.txt"], "100kb"),
            (["FILE_SEARCH_AT", "2021-07-01T12:25:00", "Up"], []),
            (["FILE_GET_AT", "2021-07-01T12:25:00", "Update2.txt"], None)
        ]
        self.assert_simulation(test_data)

if __name__ == '__main__':
    unittest.main()
