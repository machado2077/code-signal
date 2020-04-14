def matrixElementsSum(matrix):    
    soma = 0
    #validade = True
    for linha in range(0, len(matrix)):
        for col in range(0, len(matrix[linha])):            
            validade = True
            for i in range(0, linha):                                
                if matrix[i][col] == 0:               
                    validade = False
            if validade == True:                
                soma += matrix[linha][col]        
    return soma
