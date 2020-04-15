def matrixElementsSum(matrix):    
    """Função que soma os elementos de uma matriz cujos elementos acima não são nulos.
    
    Arguments:
        matrix {list} -- uma lista contendo outras listas que compõe as linhas da matriz
    
    Returns:
        int or float -- soma de todos os elementos descrito
    """
    soma = 0
    for linha in range(0, len(matrix)):
        for col in range(0, len(matrix[linha])):            
            validade = True
            for i in range(0, linha):                                
                if matrix[i][col] == 0:               
                    validade = False
            if validade == True:                
                soma += matrix[linha][col]        
    return soma

#---------------------------------------------------------------------------------
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

if __name__ == '__main__':
    unittest.main()