from matrixElementsSum import matrixElementsSum
import unittest

class matrixElementsSumTest(unittest.TestCase):
    

    samples = [
    [[0,1,1,2], [0,5,0,0], [2,0,3,3]],
    [[1,1,1,0], [0,5,0,1], [2,1,3,10]]
    ]

    def test_1(self):                    
        self.assertEqual(matrixElementsSum(self.samples[0]), 9)

    def test_2(self):
        soma = matrixElementsSum(self.samples[1])
        self.assertEqual(soma, 9)

unittest.main()