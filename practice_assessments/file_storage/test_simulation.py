import unittest

from simulation import simulate_coding_framework


class SimulationTestCase(unittest.TestCase):
    def assert_simulation(self, steps):
        """Run (command, expected_result) pairs together to preserve file state."""
        commands = [command for command, _ in steps]
        results = simulate_coding_framework(commands)

        self.assertIsInstance(results, list, "Return a list with one result per command.")
        self.assertEqual(len(results), len(steps), "Every command needs a result.")
        for index, ((command, expected), actual) in enumerate(zip(steps, results), 1):
            with self.subTest(step=index, command=command):
                self.assertEqual(actual, expected)


class TestLevel1(SimulationTestCase):
    def test_upload_get_and_copy_preserve_size(self):
        self.assert_simulation([
            (["FILE_UPLOAD", "Cars.txt", "200kb"], None),
            (["FILE_GET", "Cars.txt"], "200kb"),
            (["FILE_COPY", "Cars.txt", "Cars2.txt"], None),
            (["FILE_GET", "Cars2.txt"], "200kb"),
        ])

    def test_duplicate_upload_raises(self):
        with self.assertRaises(RuntimeError):
            simulate_coding_framework([
                ["FILE_UPLOAD", "Cars.txt", "200kb"],
                ["FILE_UPLOAD", "Cars.txt", "300kb"],
            ])

    def test_copy_missing_source_raises(self):
        with self.assertRaises(RuntimeError):
            simulate_coding_framework([
                ["FILE_COPY", "Missing.txt", "Copy.txt"],
            ])

    def test_get_missing_file_returns_none(self):
        self.assert_simulation([
            (["FILE_GET", "Missing.txt"], None),
        ])

    def test_copy_overwrites_destination_and_preserves_source(self):
        self.assert_simulation([
            (["FILE_UPLOAD", "Source.txt", "200kb"], None),
            (["FILE_UPLOAD", "Destination.txt", "100kb"], None),
            (["FILE_COPY", "Source.txt", "Destination.txt"], None),
            (["FILE_GET", "Destination.txt"], "200kb"),
            (["FILE_GET", "Source.txt"], "200kb"),
        ])


class TestLevel2(SimulationTestCase):
    def test_search_filters_by_prefix_and_orders_by_size(self):
        self.assert_simulation([
            (["FILE_UPLOAD", "Foo.txt", "100kb"], None),
            (["FILE_UPLOAD", "Bar.csv", "200kb"], None),
            (["FILE_UPLOAD", "Baz.pdf", "300kb"], None),
            (["FILE_SEARCH", "Ba"], ["Baz.pdf", "Bar.csv"]),
        ])


class TestLevel3(SimulationTestCase):
    def test_timestamped_operations_and_expired_file_lookup(self):
        # Preserve the original scenario: timestamps can move backward between
        # commands, so each operation must use its supplied timestamp.
        self.assert_simulation([
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Python.txt", "150kb"], None),
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600], None),
            (["FILE_GET_AT", "2021-07-01T13:00:01", "Python.txt"], "150kb"),
            (["FILE_COPY_AT", "2021-07-01T12:00:00", "Python.txt", "PythonCopy.txt"], None),
            (["FILE_SEARCH_AT", "2021-07-01T12:00:00", "Py"], ["Python.txt", "PythonCopy.txt"]),
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Expired.txt", "100kb", 1], None),
            (["FILE_GET_AT", "2021-07-01T12:00:02", "Expired.txt"], None),
            (["FILE_COPY_AT", "2021-07-01T12:00:00", "CodeSignal.txt", "CodeSignalCopy.txt"], None),
            (["FILE_SEARCH_AT", "2021-07-01T12:00:00", "Code"], ["CodeSignal.txt", "CodeSignalCopy.txt"]),
        ])


class TestLevel4(SimulationTestCase):
    def test_rollback_preserves_earlier_files_and_removes_later_changes(self):
        # At 12:10, Initial.txt and Update1.txt exist. Update1.txt was uploaded
        # at 12:05 with a one-hour TTL, so it is still alive at the later read.
        # The copy at 12:15 and upload at 12:20 are undone by the rollback.
        self.assert_simulation([
            (["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Initial.txt", "100kb"], None),
            (["FILE_UPLOAD_AT", "2021-07-01T12:05:00", "Update1.txt", "150kb", 3600], None),
            (["FILE_GET_AT", "2021-07-01T12:10:00", "Initial.txt"], "100kb"),
            (["FILE_COPY_AT", "2021-07-01T12:15:00", "Update1.txt", "Update1Copy.txt"], None),
            (["FILE_UPLOAD_AT", "2021-07-01T12:20:00", "Update2.txt", "200kb", 1800], None),
            (["ROLLBACK", "2021-07-01T12:10:00"], None),
            (["FILE_GET_AT", "2021-07-01T12:25:00", "Update1.txt"], "150kb"),
            (["FILE_GET_AT", "2021-07-01T12:25:00", "Initial.txt"], "100kb"),
            (["FILE_SEARCH_AT", "2021-07-01T12:25:00", "Up"], ["Update1.txt"]),
            (["FILE_GET_AT", "2021-07-01T12:25:00", "Update2.txt"], None),
        ])


if __name__ == "__main__":
    unittest.main()
