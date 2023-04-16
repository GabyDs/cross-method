def MomEmpPerf(lista_de_barras, lista_de_nodos):
    """
    Calcula los momentos de empotramiento perfecto en una lista de barras.

    Args:
    - lista_de_barras (list): Lista de barras.
    - lista_de_nodos (list): Lista de nodos.

    Returns:
    None.
    """
    
    for i in range(len(lista_de_barras)): #Recorre todas las barras
        if i==0: #Primer Barra
            if lista_de_barras[i][5] == 1: # emp-emp: M=ql^2/12
                
                lista_de_nodos[2*i]= lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 12 
                lista_de_nodos[2*i+1]= -lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 12
    
                
            elif lista_de_barras[i][5]==2: # Emp- art: M=ql^2/8
                lista_de_nodos[i]= 0
                lista_de_nodos[i+1]= -lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 8
                
            elif lista_de_barras[i][5]==3:  # Emp:libre: M=ql^2/2
                lista_de_nodos[i]= 0
                lista_de_nodos[i+1]= -lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 2

        elif i==len(lista_de_barras)-1: #Ultima barra
            if lista_de_barras[i][5]==1: # emp-emp: ql^2
                
                lista_de_nodos[2*i]= lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 12
                lista_de_nodos[2*i+1]= -lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 12
    
                
            elif lista_de_barras[i][5]==2: # Emp- art: M=ql^2/8
                lista_de_nodos[2*i+1]= 0
                lista_de_nodos[2*i]= lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 8
                
            elif lista_de_barras[i][5]==3:  # Emp:libre: M=ql^2/2
                lista_de_nodos[2*i+1]= 0
                lista_de_nodos[2*i]= lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 2
        else: #Barras intermedias
        
            if lista_de_barras[i][5]==1: # emp-emp: ql^2/12
                lista_de_nodos[2*i]= lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 12
                lista_de_nodos[2*i+1]= -lista_de_barras[i][6]*lista_de_barras[i][0]**2 / 12
