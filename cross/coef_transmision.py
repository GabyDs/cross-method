def CoefTransmision(lista_de_barras):
    """
    Calcula el coeficiente de transmisión beta de cada barra.

    Args:
    lista_de_barras: lista de listas. Cada sublista contiene los valores de una barra en el siguiente orden:
    [Longitud de la barra, Módulo de elasticidad del material, Base de la sección transversal, Altura de la sección transversal,
    Condición de borde, Carga distribuida, Fuerza concentrada, Posición de la fuerza concentrada, Coeficiente de transmisión, Coeficiente de rigidez]

    Returns:
    None
    """
    for i in range(len(lista_de_barras)):
        if lista_de_barras[i][5] == 1: # emp-emp: Beta=0.5
            lista_de_barras[i][8] = 0.5
                
        elif lista_de_barras[i][5] == 2: # Emp-art: Beta=0
            lista_de_barras[i][8] = 0
                
        elif lista_de_barras[i][5] == 3: # Emp-libre: Beta=0
            lista_de_barras[i][8] = 0