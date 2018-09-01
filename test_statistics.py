# -*- coding: utf-8 -*-

import unittest
import statistics


class TestMedian(unittest.TestCase):
    def test_median(self):
        self.numbers1 = ['2', '5', '8']
        self.numbers2 = ['2', '5', '10', '6.5']
        
        self.assertEqual([statistics.median(self.numbers1), statistics.median(self.numbers2)],
                          [5, 5.75])
        
        
class TestAverage(unittest.TestCase):
    def test_average(self):
        self.numbers1 = ['1', '2', '2.5', '3.7', '8.2']
        
        self.assertAlmostEqual(statistics.average(self.numbers1), 3.48)
        
        
class TestStdDeviation(unittest.TestCase):
    def test_average(self):
        self.numbers1 = ['1', '2', '2.5', '3.7', '8.2']
        self.average = 3.48
        
        self.assertAlmostEqual(statistics.std_deviation(self.numbers1, 3.48), 2.515)
        
if __name__ == '__main__':
    unittest.main()