def MetCross(lista_de_barras, lista_de_nodos, bal_nodal, transporte, gamma):

    """
    Calcula el momento final de una viga en sección transversal para una configuración determinada
    de nodos y barras, aplicando el método de equilibrio y transporte cruzado.

    Args:
    -----------
    lista_de_barras: list
        Lista que contiene las propiedades de cada barra. Cada elemento es una lista con las
        siguientes propiedades: [x1, y1, x2, y2, area, material, restricciones].
    lista_de_nodos: list
        Lista que contiene las coordenadas (en metros) de cada nodo. Cada elemento es una lista
        con las coordenadas x e y del nodo.
    bal_nodal: list
        Lista que contiene el balance nodal para cada nodo. Se debe pasar una lista vacía al
        inicio de la función, ya que los valores serán calculados durante la ejecución.
    transporte: list
        Lista que contiene los valores de transporte de momento para cada barra. Se debe pasar
        una lista vacía al inicio de la función, ya que los valores serán calculados durante la
        ejecución.
    gamma: list
        Lista que contiene los coeficientes gamma para cada nodo. Debe tener la misma longitud
        que la lista_de_nodos.

    Returns:
    --------
    MomFinal: list
        Lista que contiene el momento final de cada nodo. Tiene la misma longitud que la
        lista_de_nodos.
    """

    print("----------------cross----------")
    HistorialBalanceo=[]
    HistorialTransp=[]
    MomFinal=lista_de_nodos.copy()
    print("N: ", lista_de_nodos)
    print("M :", MomFinal)
    
    for i in range(0,len(lista_de_nodos),2):
        if i==0:
            bal_nodal[i+1]=(lista_de_nodos[i+1]+lista_de_nodos[i+2])*gamma[i+1]
        elif i==(len(lista_de_nodos)-2):
            bal_nodal[i]=(lista_de_nodos[i]+lista_de_nodos[(i-1)])*gamma[i]
        elif i!=0:
            bal_nodal[i+1]=(lista_de_nodos[i+1]+lista_de_nodos[i+2])*gamma[i+1]
            bal_nodal[i]=(lista_de_nodos[i]+ lista_de_nodos[(i-1)] )*gamma[i]         
        
        MomFinal[i]=MomFinal[i]+bal_nodal[i]
        MomFinal[i+1]=MomFinal[i+1]+bal_nodal[i+1]
    print("B: ", bal_nodal)
    print(MomFinal)
    
    for i in range(0,len(lista_de_nodos),2): #calculo de transporte
        if i==0:
            if lista_de_barras[i][5]==1:
                transporte.append(bal_nodal[i+1]/2)
                transporte.append(0.0)   
            else:
                transporte.append(0.0)
                transporte.append(0.0)   
        elif i==(len(lista_de_nodos)-2):
            a=i//2
            if lista_de_barras[a][5]==1:
                transporte.append(0.0)
                transporte.append(bal_nodal[i]/2)
            else:
                transporte.append(0.0)
                transporte.append(0.0)
        elif i!=0:
            transporte.append(bal_nodal[i+1]/2)
            transporte.append(bal_nodal[i]/2)  
        
        MomFinal[i]=MomFinal[i]+transporte[i]
        MomFinal[i+1]=MomFinal[i+1]+transporte[i+1]
    print("T: ", transporte)   
            
    HistorialTransp.append(transporte)
    HistorialBalanceo.append(bal_nodal)

    while True:
        
        for i in range(0,len(lista_de_nodos),2):
    
            if i==0:
                bal_nodal[i+1]=(transporte[i+1]+transporte[i+2])*gamma[i+1]
            elif i==(len(lista_de_nodos)-2):
                bal_nodal[i]=(transporte[i]+transporte[i-1])*gamma[i]
            elif i!=0:
                bal_nodal[i+1]=(transporte[i+1]+transporte[i+2])*gamma[i+1]
                bal_nodal[i]=(transporte[i]+transporte[i-1])*gamma[i]    
        
            MomFinal[i]=MomFinal[i]+bal_nodal[i]
            MomFinal[i+1]=MomFinal[i+1]+bal_nodal[i+1]
        
        #HistorialBalanceo.append(BalNodal)
        print("B: ", bal_nodal)
        
        if max(bal_nodal)<0.01 and min(bal_nodal)>-0.01:    
            break
        
        for i in range(0,len(lista_de_nodos),2): #calculo de transporte
            if i==0:
                a=i//2
                if lista_de_barras[a][5]==1:
                    transporte[i]=bal_nodal[i+1]/2
            elif i==(len(lista_de_nodos)-2):
                a=i//2
                if lista_de_barras[a][5]==1:
                    transporte[i+1]=bal_nodal[i]/2
            elif i!=0:
                transporte[i+1]=bal_nodal[i]/2
                transporte[i]=bal_nodal[i+1]/2
                
            MomFinal[i]+=transporte[i]
            MomFinal[i+1]=MomFinal[i+1]+transporte[i+1]
            
        print("T: ", transporte)
    
        #HistorialTransp.append(Transporte)
    print("MOMENTO FINAL: ",MomFinal)