import unittest
import groups

class TestCases(unittest.TestCase):
   def test_group_of_3(self):
      self.assertEqual(groups.groups_of_3([1,2,3,4,5,6,7,8,9]),[[1,2,3],[4,5,6],[7,8,9]])
      self.assertEqual(groups.groups_of_3([1,2,3,4,5,6,7]),[[1,2,3],[4,5,6],[7]])
      self.assertEqual(groups.groups_of_3([1,2,3]),[[1,2,3]])
      pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
