def isLucky(n):
    cont_first = cont_second = 0    
    #iterar sobre a primeira metade do numero, somando os elementos
    #obter o tamanho do numero
    for num_first in range(0, len(f'{n}')//2):
        cont_first += int(f'{n}'[num_first])
    
    #iterar sobre a segunda metade o numero, somando os elementos
    for num_second in range(len(f'{n}')//2, len(f'{n}')):
        cont_second += int(f'{n}'[num_second])

    #comparar a duas somas
    if cont_first == cont_second:
        return True
    else:
        return False


print(isLucky(1230))