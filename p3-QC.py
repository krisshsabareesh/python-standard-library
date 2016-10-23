#Quality Control

def average(values) :
  """ Computes Arithmetic mean of a list of numbers
  >>> print(average([20, 30, 40, 50, 60, 70]))
  45.0
  """
  return sum(values) / len(values)
import doctest
doctest.testmod()  ##Automatically validate embedded tests

import unittest
class TestStaticalFunctions(unittest.TestCase) :
  def testAverage(self) :
    """average() should give known result for known values"""
    self.assertEqual(average([20, 30, 70]), 40.0)
    self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
    with self.assertRaises(ZeroDivisionError) :
      average([])
    with self.assertRaises(TypeError) :
      average(20, 30, 70)
unittest.main()    ##invokes all tests
