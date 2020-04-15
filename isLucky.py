def isLucky(n):
    cont_first = cont_second = 0    
    #iterar sobre a primeira metade do numero, somando os elementos
        #obter o tamanho do numero, transformando-o em string
    for num_first in range(0, len(f'{n}')//2):
        cont_first += int(f'{n}'[num_first])
    
    #iterar sobre a segunda metade do numero, somando os elementos
    for num_second in range(len(f'{n}')//2, len(f'{n}')):
        cont_second += int(f'{n}'[num_second])

    #comparar a duas somas
    if cont_first == cont_second:
        return True
    else:
        return False

#--------------------------------------------------------------
import unittest

class inLuckyTest(unittest.TestCase):

    samples = [
        1230, 239017, 134008, 10, 11, 1010, 
        261534, 100000, 999999, 123321
    ]

    def test_1(self):
        self.assertEqual(isLucky(self.samples[0]), True)

    def test_2(self):
        self.assertEqual(isLucky(self.samples[1]), False)

    def test_3(self):
        self.assertEqual(isLucky(self.samples[2]), True)

    def test_4(self):
        self.assertEqual(isLucky(self.samples[3]), False)

    def test_5(self):
        self.assertEqual(isLucky(self.samples[4]), True)

    def test_6(self):
        self.assertEqual(isLucky(self.samples[5]), True)

    def test_7(self):
        self.assertEqual(isLucky(self.samples[6]), False)

    def test_8(self):
        self.assertEqual(isLucky(self.samples[7]), False)

    def test_9(self):
        self.assertEqual(isLucky(self.samples[8]), True)

    def test_10(self):
        self.assertEqual(isLucky(self.samples[9]), True)

if __name__ == '__main__':
    unittest.main()