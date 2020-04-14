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
