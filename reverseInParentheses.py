    #TENTAR UMA VARREDURA DO TIPO:
''' 
    - inicio = fim = 0
    - enquanto houver brackets, a varredura continua
        - se o próximo bracket for == (, inicio = i
        - se o próximo bracket for == ), fim = i
             VARREDURAS SUCESSIVAS
            -a palavra partindo do (inicio + 1) ao (fim - 1) será invertida
            - remover os brackets referentes aos indices (inicio e fim)
            - break no laço interno
'''

def reverseInParentheses(inputString):    
    """Função que inverte a string dentro de parenteses.
    
    Arguments:
        inputString {string} -- string de entrada.
    
    Returns:
        string -- string formatada de acordo com o objetivo.
    """
    listaStr = list(inputString)
    inputString = ''
    inicio = fim = 0
    while True:
        if not ('(' and ')') in listaStr:
            break
        for i in range(len(listaStr)):
            if listaStr[i] == '(':
                inicio = i
            elif listaStr[i] == ')':
                fim = i
                listaStr[inicio+1:fim] = listaStr[fim-1:inicio:-1]
                del listaStr[inicio]
                del listaStr[fim-1]
                break
    for element in listaStr:
            inputString += element
    return inputString

#-----------------------------------------------------------------------
import unittest

class reverseInParenthesesTest(unittest.TestCase):

    samples = [
        "(bar)", "foo(bar)baz", "foo(bar)baz(blim)", 
        "foo(bar(baz))blim", "", "()", "(abc)d(efg)"
    ]

    def test_1(self):
        self.assertEqual(reverseInParentheses(self.samples[0]), "rab")

    def test_2(self):
        self.assertEqual(reverseInParentheses(self.samples[1]), "foorabbaz")

    def test_3(self):
        self.assertEqual(reverseInParentheses(self.samples[2]), "foorabbazmilb")

    def test_4(self):
        self.assertEqual(reverseInParentheses(self.samples[3]), "foobazrabblim")

    def test_5(self):
        self.assertEqual(reverseInParentheses(self.samples[4]), "")

    def test_6(self):
        self.assertEqual(reverseInParentheses(self.samples[5]), "")

    def test_7(self):
        self.assertEqual(reverseInParentheses(self.samples[6]), "cbadgfe")


if __name__ == '__main__':
    unittest.main()