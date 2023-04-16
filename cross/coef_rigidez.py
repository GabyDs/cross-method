def CoefRigidez(lista_de_barras):
    """
    Calcula el coeficiente de rigidez angular para cada barra.

    Args:
    lista_de_barras (list): Lista que contiene la información de cada barra de la estructura.

    Returns:
    none
    """
    for i in range(len(lista_de_barras)):
        if lista_de_barras[i][5] == 1:  # emp-emp: alpha=4EJ/L
            lista_de_barras[i][9] = (4 * lista_de_barras[i][1] * 1e9 * lista_de_barras[i][4]) / lista_de_barras[i][0]
        elif lista_de_barras[i][5] == 2:  # emp-art: alpha=3EJ/L
            lista_de_barras[i][9] = (3 * lista_de_barras[i][1] * 1e9 * lista_de_barras[i][4]) / lista_de_barras[i][0]
        elif lista_de_barras[i][5] == 3:  # emp:libre: alpha=0 (No hay rigidez angular)
            lista_de_barras[i][9] = 0