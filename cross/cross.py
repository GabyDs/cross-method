# Importaciones de las funciones necesarias
import long_barra, carga_elasticidad, dimensiones_barra, coef_rigidez
import coef_transmision, coef_distribucion, carga_distribuida, mom_emp_perfecto
import condicion_borde, metodo_cross

# Iniciar el número de barras
while True:
    numero_de_barras = int(input("Ingrese el número entero positivo de barras: "))
    if numero_de_barras > 0:
        break

# Inicializar listas
lista_de_barras = []
lista_de_nodos = []
bal_nodal = []
transporte = []
gamma = []

# Inicializar la lista de barras y nodos
for i in range(numero_de_barras):
    lista_de_barras.append([0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, [1,1], 0.00, 0.00])
    # lista_de_barras = [[L, E, b, h, J, CondBorde, q, [x,p], Beta, Alpha], ...]
    lista_de_nodos.append(0)
    lista_de_nodos.append(0)
    
# Copiar la lista de nodos
bal_nodal = lista_de_nodos.copy()

# Copiar la lista de nodos
gamma = lista_de_nodos.copy()

# Crear la lista de transporte
transporte = []

#Carga longitud de barra       
long_barra.cargar_longitud(numero_de_barras, lista_de_barras)

#Cargar modulo de elasticidad de las barras
carga_elasticidad.CargaE(lista_de_barras)

#Cargar dimensiones de cada barra
dimensiones_barra.cargar_dimensiones(lista_de_barras)

#Seleccion de condicion de borde de cada Barra
condicion_borde.CondicionesDeBorde(lista_de_barras)

# Calcula el coeficiente de rigidez de cada barra
coef_rigidez.CoefRigidez(lista_de_barras)

# Calcula el coeficiente de transmision
coef_transmision.CoefTransmision(lista_de_barras)

# Calcula el coeficiente de distribucion de cada barra
gamma = coef_distribucion.coef_distribucion(lista_de_barras, lista_de_nodos)

# Carga distribuida de cada barra
carga_distribuida.carga_distribuida(lista_de_barras)

# Carga el momento de empotramiento perfecto de cada barra
mom_emp_perfecto.MomEmpPerf(lista_de_barras, lista_de_nodos)

# Metodo de CROSS
metodo_cross.MetCross(lista_de_barras, lista_de_nodos, bal_nodal, transporte, gamma)