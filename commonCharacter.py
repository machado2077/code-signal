def commonCharacterCount(s1, s2):
    """Função que retorna o número de caracteres e sua quantidade entre duas strings
    
    Arguments:
        s1 {[type]} -- [description]
        s2 {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    cont = 0    
    conj = set(s1)
    for carac in conj:
        if carac in s2:
            cont += min(s1.count(carac), s2.count(carac))
    return cont

#------------------------------------------------------------------

import unittest

class commonCharacterCountTest(unittest.TestCase):

    samples = [
        {"s1": "aabcc", "s2": "adcaa"},
        {"s1": "zzzz", "s2": "zzzzzzz"},
        {"s1": "abca", "s2": "xyzbac"},
        {"s1": "a", "s2": "b"},
        {"s1": "a", "s2": "aaa"}
    ]

    def test_1(self):
        self.assertEqual(commonCharacterCount(self.samples[0]["s1"], self.samples[0]["s2"]), 3)
        
    def test_2(self):
        self.assertEqual(commonCharacterCount(self.samples[1]["s1"], self.samples[1]["s2"]), 4)

    def test_3(self):
        self.assertEqual(commonCharacterCount(self.samples[2]["s1"], self.samples[2]["s2"]), 3)

    def test_4(self):
        self.assertEqual(commonCharacterCount(self.samples[3]["s1"], self.samples[3]["s2"]), 0)

    def test_5(self):
        self.assertEqual(commonCharacterCount(self.samples[4]["s1"], self.samples[4]["s2"]), 1)


if __name__ == '__main__':
    unittest.main()