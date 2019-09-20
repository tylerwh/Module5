import unittest
from input_loops import average_input_scores


class MyTestCase(unittest.TestCase):


  def test_average(self):
    self.assertEqual(77.2, average_input_scores.average([88, 90, 75, 62.5, 70.5]))


if __name__ == "__main__":
    unittest.main()