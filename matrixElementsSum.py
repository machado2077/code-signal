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
                print('\n', matrix[linha][col])
                soma += matrix[linha][col]
        #validade = True        
    return soma

m = [
    [0,1,1,2], 
    [0,5,0,0], 
    [2,0,3,3]
 ]

r = matrixElementsSum(m)
print()
print(r)