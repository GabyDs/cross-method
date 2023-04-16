def coef_distribucion(lista_de_barras, lista_de_nodos):
    """
    Calcula los coeficientes de distribución Gamma para cada barra, basado en los valores de rigidez angular
    de cada barra y los nodos adyacentes.

    Args:
    - lista_de_barras: lista que contiene las características de cada barra, en el orden [L, E, A, I, phi, c, 0, 0, beta, alpha].
    - lista_de_nodos: lista que contiene la posición de los nodos en el eje x.

    Returns:
    - gamma: lista que contiene los coeficientes de distribución Gamma para cada barra, en el orden [Gamma_0, Gamma_1, Gamma_1, Gamma_2, ...]
    """
    gamma = []

    for i in range(len(lista_de_barras)):
        if i == 0:  
            gamma.append(0)
            gamma.append(-lista_de_barras[i][9]/(lista_de_barras[i][9] + lista_de_barras[i+1][9]))

        elif i == (len(lista_de_barras)-1):
            gamma.append(-lista_de_barras[i][9]/(lista_de_barras[i-1][9] + lista_de_barras[i][9]))
            gamma.append(0)

        else:
            gamma.append(-lista_de_barras[i][9]/(lista_de_barras[i-1][9] + lista_de_barras[i][9]))
            gamma.append(-lista_de_barras[i][9]/(lista_de_barras[i][9] + lista_de_barras[i+1][9]))

    return gamma