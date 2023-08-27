import unittest
import practice

class IsEqual(unittest.TestCase):

    def testIsEqual(self):
        answer = practice.isEqual(1, 1)
        self.assertTrue(answer)
        
    def testIsEqual(self):
        answer = practice.isEqual(1, 2)
        self.assertFalse(answer)

if __name__ == "__main__":
    unittest.main()