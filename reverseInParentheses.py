<<<<<<< HEAD
# BRANCH: reverseV3    
    #TENTAR UMA VARREDURA DO TIPO:
''' 
    - inicio = fim = 0
    - enquanto houver brackets, a varredura continua
        - se o próximo bracket for == (, inicio = i
        - se o próximo bracket for == ), fim = i
             VARREDURAS SUCESSIVAS
            -a palavra partindo do inicio ao fim será ivertida
            - remover os brackets referentes aos indices (inicio e fim)
            - break no laço interno
'''

def reverseInParentheses(inputString):    
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
=======
def reverseInParentheses(inputString):
    #branch: reverseV2
    #varrer a string e mapear os () 
    #inserir os "(" em um coordenadas bem como os ")"
    #unir os () extremos 
    map_open = []  
    map_close = []
    for i in range(0, len(inputString)):
        if inputString[i] == '(':
            map_open.append(i)
        elif inputString[i] == ')':
            map_close.append(i)
    #inverter as strings dos () internos para os externos
    #(bar(baz))  ; a = [0, 4], b = [8, 9]   => [4, 0], [8, 9] resolve => (4, 8),                                                                    (0, 9)
        # nesse caso, a[1] < b[0]
    #(bar)baz(blim) ; a = [0, 8], b = [4, 13] => (0, 4), (8, 13)
        #nesse caso, a[1] > a[0]

    # (bar(kor)(zir)) ; a = [0, 4, 8], b = [7, 12, 13] => (0, 13), (4, 7), (8, 12)
        #nesse caso, a[1] < b[0]
    
>>>>>>> reverseV2
