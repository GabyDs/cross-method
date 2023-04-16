def CargaE(lista_de_barras):
    """
    Carga el módulo de elasticidad (E) de las barras.

    Args:
        lista_de_barras (list): La lista de barras.

    Returns:
        None.
    """
    E_bool = int(input("¿Todas las barras tienen el mismo Modulo de Elasticidad (E)? (0 = No, 1 = Si): "))
    if E_bool == 1:
        E = float(input("Inserte el valor de E: "))
        for i in range(len(lista_de_barras)):
            lista_de_barras[i][1] = E
    elif E_bool == 0:
        for i in range(len(lista_de_barras)):
            lista_de_barras[i][1] = float(input("Inserte el valor de E de la barra {}: ".format(i+1)))
    else:
        print("Opción inválida. Intente de nuevo.")
        CargaE(lista_de_barras)