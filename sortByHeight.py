"""
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""

def sortByHeight(a):    
    #verificar se há -1 na lista. havendo, mapear seus indices
    #se não haver, retornar a lista com sorted
    ordenados = [
        a[i] 
        for i in range(0, len(a)) 
        if a[i] != -1
        ]
    #gerar uma outra lista ordenada com sort
    ordenados.sort()
    #realizar um laço para dar um replace no elementos 0
    n = 0
    for i in range(0, len(a)):
        if a[i] != -1:
            a[i] = ordenados[n]
            n += 1
    return a        