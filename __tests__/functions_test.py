import unittest
from utils.general import *


class TestThreshold(unittest.TestCase):

    def test_threshold_above(self):
        self.assertEqual(change_above_threshold(100, 105, 5), True, "Should return true if % change is >= threshold")
        self.assertEqual(change_above_threshold(100, 90, 10), True, "Should return true if % change is >= threshold")

    def test_threshold_below(self):
        self.assertEqual(change_above_threshold(100, 101, 5), False, "Should return false if % change is < threshold")
        self.assertEqual(change_above_threshold(100, 99, 5), False, "Should return false if % change is < threshold")


class TestTrainingData(unittest.TestCase):

    def test_look_back_1(self):
        x_data, y_data = [0, 1, 2, 3, 4, 5], [2, 4, 2, 3, 1, 2]
        x_train, y_train = training_data_for_t(data=(x_data, y_data), t=2, look_back=-1)

        self.assertEqual(x_train, [0, 1], "Should return [0, 1] as training x data for t=2")
        self.assertEqual(y_train, [2, 4], "Should return [2, 4] as training y data for t=2")

    def test_look_back_2(self):
        x_data, y_data = [0, 1, 2, 3, 4, 5], [2, 4, 2, 3, 1, 2]
        x_train, y_train = training_data_for_t(data=(x_data, y_data), t=3, look_back=10)

        self.assertEqual(x_train, [0, 1, 2], "Should return [0, 1, 2] as training x data for t=3")
        self.assertEqual(y_train, [2, 4, 2], "Should return [2, 4, 2] as training y data for t=3")


if __name__ == '__main__':
    unittest.main()
