#aabcc      e       adcaa   = 3: 2a,1c

def commonCharacterCount(s1, s2):
    cont = 0    
    conj = set(s1)
    for carac in conj:
        if carac in s2:
            cont += min(s1.count(carac), s2.count(carac))
    return cont