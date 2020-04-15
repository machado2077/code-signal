def allLongestStrings(inputArray):
    """Função que retorna a(s) maior(es) string(s) em um dado vetor.
    
    Arguments:
        inputArray {array} -- uma lista contendo strings.
    
    Returns:
        array -- uma lista contendo a(s) maior(es) string(s) do array inserido.
    """
    
    tam = []
    for item in inputArray:
        tam.append(len(item))    
    strings = [item for item in inputArray if len(item) == max(tam)]
    return strings

#----------------------------------------------------------------------------------------
import unittest

class allLongestStringsTest(unittest.TestCase):
    
    samples = [
        ["aba", "aa", "ad", "vcd", "aba"],
        ["aa"],
        ["abc", "eeee", "abcd", "dcd"]
    ]

    def test_1(self):
        self.assertEqual(allLongestStrings(self.samples[0]), ["aba", "vcd", "aba"])

    def test_2(self):
        self.assertEqual(allLongestStrings(self.samples[1]), ["aa"])
    
    def test_3(self):
        self.assertEqual(allLongestStrings(self.samples[2]), ["eeee", "abcd"])

if __name__ == '__main__':
    unittest.main()



