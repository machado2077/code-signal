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