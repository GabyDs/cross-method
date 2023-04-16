def cargar_dimensiones(lista_de_barras):
    """
    Carga las dimensiones de cada sección transversal de las barras, calcula su inercia
    y las agrega a la lista de barras.

    Args:
        lista_de_barras (list): La lista de barras.
    """
    for i in range(len(lista_de_barras)):
        while True:
            base = float(input("Inserte la base en cm de la sección de la barra {}: ".format(i+1)))
            altura = float(input("Inserte la altura en cm de la sección de la barra {}: ".format(i+1)))
            if base > 0 and altura > 0:
                inercia = ((base * altura**3) / 12) / 10**8  # Calcula la inercia de la sección en m^4
                lista_de_barras[i][2] = base
                lista_de_barras[i][3] = altura
                lista_de_barras[i][4] = inercia
                break
            print("Error, valor negativo o cero")