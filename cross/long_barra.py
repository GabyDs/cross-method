def cargar_longitud(numero_de_barras, lista_de_barras):
    """
    Carga la longitud de la barra 'i' y la agrega a la lista de barras.

    Args:
        lista_de_barras (list): La lista de barras.
        i (int): El índice de la barra a la que se agregará la longitud.
    """
    for i in range(numero_de_barras):
        while True:
            longitud = float(input("Ingrese la longitud de la barra {} en metros: ".format(i+1)))
            if longitud > 0:
                break
            print("La longitud debe ser un número positivo distinto de cero.")
        
        lista_de_barras[i][0] = longitud