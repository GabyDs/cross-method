def CondicionesDeBorde(lista_de_barras):
    """
    Esta función permite al usuario elegir la condición de borde de cada barra de la estructura.

    Args:
    lista_de_barras (list): Lista que contiene la información de cada barra de la estructura.

    Returns:
    None
    """
    for i in range(len(lista_de_barras)):   
        while True:
            print("Escoge la condicion de borde de las barra {}: ".format(i+1))
            print("1) Empotrada-empotrado")
            print("2) Empotrada-articulado")
            opcion = int(input("3) Empotrada-Libre\n-> "))
            
            if opcion== 1 or opcion== 2 or opcion== 3: #Validacion
                lista_de_barras[i][5]=opcion
                break
            print("Escoja una opcion correcta")