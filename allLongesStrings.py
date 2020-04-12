def allLongestStrings(inputArray):
    tam = []
    #varrer a lista coletando o tamanho de todos os itens
    for item in inputArray:
        tam.append(len(item))
    #realizar uma segunda varredura para obter uma outra lista apenas com os itens com maiores comprimentos
    strings = [item for item in inputArray if len(item) == max(tam)]
    return strings