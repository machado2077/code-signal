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
    