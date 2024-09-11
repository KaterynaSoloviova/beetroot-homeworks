# Task 1
# Pick your solution to one of the exercises in this module. Design tests for this solution and write tests
# using unittest library (with setUp and tearDown)

from tvcontroller import TVController
import unittest


class TestTVController(unittest.TestCase):

    def setUp(self):
        self.controller = TVController(["BBC", "Discovery", "TV1000"])

    def tearDown(self):
        self.controller.first_channel()

    def test_current_channel(self):
        res = self.controller.current_channel()

        self.assertEqual(res, "BBC")

    def test_first_channel(self):
        res = self.controller.first_channel()

        self.assertEqual(res, "BBC")

    def test_last_channel(self):
        res = self.controller.last_channel()

        self.assertEqual(res, "TV1000")

    def test_turn_channel(self):
        res = self.controller.turn_channel(2)

        self.assertEqual(res, "Discovery")

    def test_turn_channel_not_exist(self):
        try:
            self.controller.turn_channel(10)
        except ValueError as e:
            self.assertEqual(str(e), "Channel 10 is not in ['BBC', 'Discovery', 'TV1000']")

    def test_next_channel(self):
        res = self.controller.next_channel()

        self.assertEqual(res, "Discovery")


if __name__ == "__main__":
    unittest.main()
