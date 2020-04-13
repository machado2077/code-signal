def reverseInParentheses(inputString):
    # BRANCH: reverseV3
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
    #(bar(baz))  = [0, 4], [8, 9]   => [4, 0], [8, 9] resolve
    
    #(bar)baz(blim) = [0, 8], [4, 13]