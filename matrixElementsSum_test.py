from matrixElementsSum import matrixElementsSum
import unittest

class matrixElementsSumTest(unittest.TestCase):

    samples = [
    [[0,1,1,2], [0,5,0,0], [2,0,3,3]],
    [[1,1,1,0], [0,5,0,1], [2,1,3,10]]
    ]

    def test_matrixElementsSum(self):        
        
        #Test 1
        test_1 = matrixElementsSum(self.samples[0])
        self.assertEqual(test_1, 9)

        #Test 2
        test_2 = matrixElementsSum(self.samples[1])
        self.assertEqual(test_2, 9)

unittest.main()