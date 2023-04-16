def carga_distribuida(lista_de_barras):
    """Carga de carga distribuida "q" en cada barra.

    Args:
        lista_de_barras (list): Lista de barras.

    Returns:
        None.

    """
    for i in range(len(lista_de_barras)):
        while True:
            carga = float(input(f"Ingrese carga distribuida de la barra {i+1}: "))
            if carga > 0:
                lista_de_barras[i][6] = carga
                break
            else:
                print("Error: la carga debe ser positiva.")