def sortByHeight(a):  
    """Função que ordena pessoas entre árvores (-1) por tamanho (números) 
    
    Arguments:
        a {array} -- lista contendo os elementos do conjunto pessoas-árvore dispostas em fila 
    
    Returns:
        array -- uma lista contendo o conjunto inicial ordenado
    """
    ordenados = [
        a[i] 
        for i in range(0, len(a)) 
        if a[i] != -1
        ]
    ordenados.sort()
    n = 0
    for i in range(0, len(a)):
        if a[i] != -1:
            a[i] = ordenados[n]
            n += 1
    return a        

#------------------------------------------------------------------------
import unittest

class sortByHeightTest(unittest.TestCase):

    samples = [
        [-1, 150, 190, 170, -1, -1, 160, 180],
        [-1, -1, -1, -1, -1], [-1],
        [4, 2, 9, 11, 2, 16],
        [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
    ]

    def test_1(self):
        self.assertEqual(sortByHeight(self.samples[0]), [-1, 150, 160, 170, -1, -1, 180, 190])

    def test_2(self):
        self.assertEqual(sortByHeight(self.samples[1]), [-1, -1, -1, -1, -1])

    def test_3(self):
        self.assertEqual(sortByHeight(self.samples[2]), [-1])

    def test_4(self):
        self.assertEqual(sortByHeight(self.samples[3]), [2, 2, 4, 9, 11, 16])

    def test_5(self):
        self.assertEqual(sortByHeight(self.samples[4]), [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2])

    def test_6(self):
        self.assertEqual(sortByHeight(self.samples[5]), [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77])

if __name__ == '__main__':
    unittest.main()