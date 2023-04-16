'''Elemento de de matriz barra: 
    [[Longitud , E, b , h, J , CondDeBorde, carga_distribuida , [distancia , Carga_puntual],Coef_transmision, coef_rigidez],[ .... ]

*La condicion de borde se reprensenta por los siguientes numeros:
    1) Empotrada-empotrada
    2) Empotrada-articulado
    3) Empotrada-Libre

Elemento de la matriz nodos:
    [Numero de nodo, coef_distribucion, Momento_Empotramiento_Perfecto, Momento_Final]
'''




def CargaPuntual (Barra):
    Barra[i][7][0]= float(input("Inserte distancia del nodo {} de la carga puntual de la barra {}:  ".format(i+1,Barra[i])))
    Barra[i][8][1]= float(input("Inserte carga distribuida de la barra {}:  ".format(Barra[i])))

def MetCross(Barra):
    print("----------------cross----------")
    HistorialBalanceo=[]
    HistorialTransp=[]
    MomFinal=Nodos.copy()
    print("N: ",Nodos)
    print("M :",MomFinal)
    
    for i in range(0,len(Nodos),2):

        if i==0:
            BalNodal[i+1]=(Nodos[i+1]+Nodos[i+2])*Gamma[i+1]
        elif i==(len(Nodos)-2):
            BalNodal[i]=(Nodos[i]+Nodos[(i-1)])*Gamma[i]
        elif i!=0:
            BalNodal[i+1]=(Nodos[i+1]+Nodos[i+2])*Gamma[i+1]
            BalNodal[i]=(Nodos[i]+ Nodos[(i- 1)] )*Gamma[i]         
        
        MomFinal[i]=MomFinal[i]+BalNodal[i]
        MomFinal[i+1]=MomFinal[i+1]+BalNodal[i+1]
    print("B: ", BalNodal)
    print(MomFinal)
    
    for i in range(0,len(Nodos),2): #calculo de transporte
    
        if i==0:
            
            if Barra[i][5]==1:
                Transporte.append(BalNodal[i+1]/2)
                Transporte.append(0.0)   
            else:
                Transporte.append(0.0)
                Transporte.append(0.0)
                
            
        elif i==(len(Nodos)-2):
            a=i//2
            
            if Barra[a][5]==1:
                Transporte.append(0.0)
                Transporte.append(BalNodal[i]/2)
            else:
                Transporte.append(0.0)
                Transporte.append(0.0)
                
        elif i!=0:
            Transporte.append(BalNodal[i+1]/2)
            Transporte.append(BalNodal[i]/2)  
        
        MomFinal[i]=MomFinal[i]+Transporte[i]
        MomFinal[i+1]=MomFinal[i+1]+Transporte[i+1]
    print("T: ", Transporte)   
            
            
    HistorialTransp.append(Transporte)
    HistorialBalanceo.append(BalNodal) 
    
    while True:
        
        for i in range(0,len(Nodos),2):
    
            if i==0:
                BalNodal[i+1]=(Transporte[i+1]+Transporte[i+2])*Gamma[i+1]
            elif i==(len(Nodos)-2):
                BalNodal[i]=(Transporte[i]+Transporte[i-1])*Gamma[i]
            elif i!=0:
                BalNodal[i+1]=(Transporte[i+1]+Transporte[i+2])*Gamma[i+1]
                BalNodal[i]=(Transporte[i]+Transporte[i-1])*Gamma[i]    
        
            MomFinal[i]=MomFinal[i]+BalNodal[i]
            MomFinal[i+1]=MomFinal[i+1]+BalNodal[i+1]
        
        #HistorialBalanceo.append(BalNodal)
        print("B: ", BalNodal)
        
        if max(BalNodal)<0.01 and min(BalNodal)>-0.01:    
            break
        
        for i in range(0,len(Nodos),2): #calculo de transporte
            if i==0:
                a=i//2
                if Barra[a][5]==1:
                    Transporte[i]=BalNodal[i+1]/2
            elif i==(len(Nodos)-2):
                a=i//2
                if Barra[a][5]==1:
                    Transporte[i+1]=BalNodal[i]/2
            elif i!=0:
                Transporte[i+1]=BalNodal[i]/2
                Transporte[i]=BalNodal[i+1]/2
                
            MomFinal[i]+=Transporte[i]
            MomFinal[i+1]=MomFinal[i+1]+Transporte[i+1]
            
        print("T: ", Transporte)
    
        #HistorialTransp.append(Transporte)
    print("MOMENTO FINAL: ",MomFinal)


#----------------------------------------------Funcion Main -------------------------------------------------------------------#

#Iniciamos la matriz barra con su numero barras totales   
while True:
    n=int(input("Inserte numero de barras: "))
    if n>0: #Validacion 
        break

# Inicializacion de listas     
Barra=[] 
Nodos=[]

#Crea las listas Barra y Nodos con el vector cero para todos los paramentros de la barra [[0,0,0,0,0,[0,0],0,0],...]
#Nodo = [Numeros de barras x2]

for i in range(n): 
    Barra.append([0.00,0.00,0.00,0.00,0.00,   0.00   ,0.0, [1,1],0.00, 0.00 ])
    #Barra=[[  L ,  E ,  b , h  ,  J , CondBorde, q , [x,p],Beta, Alpha],[ .... ]
    Nodos.append(0)
    Nodos.append(0)
    
BalNodal=Nodos.copy()
Transporte=[]
Gamma=Nodos.copy()


#Muestra la lista vacia
for i in range(len(Barra)):
    print(Barra[i])
print(len(Nodos))

def CargaLongitud(Barra,a):
    j = a
    #"aqui se carga la longitud [m] y se agrega a la matriz"
    l=int(input("Inserte la longitud de la barra {}:  ".format(a)))
    Barra[j][0]=l

#Carga de datos de barra
for i in range(n):         
    CargaLongitud(Barra,i)

def CargaE (Barra): #modulo de elasticidad en [Gpa]
    E_bool = str(input("¿Todas las barras tienen el mismo Modulo de Elasticidad (E)? (Si/No):  "))
    if E_bool == "Si" or E_bool=="si":
        E=float(input("Inserte valor de E:  "))
        for i in range(len(Barra)):
            Barra[i][1]=E
    elif E_bool == "No" or E_bool== "no":
        for i in range(len(Barra)):
            Barra[i][1] = float(input("Inserte el valor de E de la barra{}:  ").format(i+1))

#Funciones
CargaE(Barra)

def CargaDimensiones (Barra): #Carga de dimensiones [cm]
    for i in range(len(Barra)):
        while True:
            Barra[i][2]= float(input("inserte la base en cm de la seccion de la barra {}: ".format(i+1))) #Carga base
            Barra[i][3]= float(input("inserte la Altura en cm de la seccion de la barra {}: ".format(i+1))) #Carga Altura
            Barra[i][4]=((Barra[i][2]*Barra[i][3]**3)/12)/100000000 #calculo de inercia de la seccion [m^4]
            if Barra[i][2] > 0 and Barra[i][3]>0: #Validacion
                break
            print("Error, valor negativo o cero")

CargaDimensiones(Barra)      #Carga de dimensiones: Base y altura. Calculo de inercia J

def CondicionesDeBorde (Barra):
    for i in range(len(Barra)):   
        while True:
            print("Escoge la condicion de borde de las barra {}: ".format(i))
            print("1) Empotrada-empotrado")
            print("2) Empotrada-articulado")
            opcion = int(input("3) Empotrada-Libre \n "))
            
            if opcion== 1 or opcion== 2 or opcion== 3: #Validacion
                Barra[i][5]=opcion
                break
            print("Escoja una opcion correcta")

CondicionesDeBorde(Barra)    #Seleccion de condicion de borde de cada Barra

def CoefRigidez(Barra): #Coeficiente de rigidez angular en Nm 
    for i in range(len(Barra)):
        if Barra[i][5]==1: # emp- emp: alpha= 4EJ/L
            Barra[i][9]=(4*Barra[i][1]*1000000000*Barra[i][4])/Barra[i][0]
            
        elif Barra[i][5]==2: # Emp- art: alpha= 3EJ/L
            Barra[i][9]=(3*Barra[i][1]*1000000000*Barra[i][4])/Barra[i][0]
            
        elif Barra[i][5]==3:  # Emp:libre: alpha= 0 (No hay rigidez angular)
            Barra[i][9]=(3*Barra[i][1]*1000000000*Barra[i][4])/Barra[i][0]

CoefRigidez(Barra)           #Calculo de coeficiente de rigidez de cada barra

def CoefTransmision (Barra): #Coef de transmicion beta
    for i in range(len(Barra)):
            if Barra[i][5]==1: # emp-emp: Beta=0.5
                Barra[i][8]=0.5
                
            elif Barra[i][5]==2: # Emp- art: Beta=0
                Barra[i][8]=0
                
            elif Barra[i][5]==3:  # Emp:libre: Beta=0
                Barra[i][8]=0

CoefTransmision(Barra)

def coef_distribucion(Barra, Nodos):
    for i in range(len(Barra)):

        if i==0:  
            Gamma[2*i]=0
            Gamma[2*i+1]=-Barra[i][9]/(Barra[i][9]+Barra[i+1][9])
        

        elif i==(len(Barra)-1):
            
            Gamma[2*i]=-Barra[i][9]/(Barra[i-1][9]+Barra[i][9])
            Gamma[2*i+1]=0
            
        else:
            Gamma[2*i]=-Barra[i][9]/(Barra[i-1][9]+Barra[i][9])
            Gamma[2*i+1]=-Barra[i][9]/(Barra[i][9]+Barra[i+1][9])
    print("Gamma: {} ".format(Gamma))

coef_distribucion(Barra, Nodos)

def CargaDistribuida (Barra): #Carga de carga distruida "q"
    for i in range(len(Barra)):
        Barra[i][6]= float(input("Inserte carga distribuida de la barra {}:  ".format(i)))

CargaDistribuida(Barra)     #Carga de "carga distriuida" en cada barra
#CargaPuntual(Barra)        #Carga de "carga puntual" de cada barra

def MomEmpPerf (Barra):
    
    for i in range(len(Barra)): #Recorre todas las barras
        if i==0: #Primer Barra
            if Barra[i][5] == 1: # emp-emp: M=ql^2/12
                
                Nodos[2*i]= Barra[i][6]*Barra[i][0]**2 / 12 
                Nodos[2*i+1]= -Barra[i][6]*Barra[i][0]**2 / 12
    
                
            elif Barra[i][5]==2: # Emp- art: M=ql^2/8
                Nodos[i]= 0
                Nodos[i+1]= -Barra[i][6]*Barra[i][0]**2 / 8
                
            elif Barra[i][5]==3:  # Emp:libre: M=ql^2/2
                Nodos[i]= 0
                Nodos[i+1]= -Barra[i][6]*Barra[i][0]**2 / 2

        elif i==len(Barra): #Ultima barra
            if Barra[i][5]==1: # emp-emp: ql^2
                
                Nodos[2*i]= Barra[i][6]*Barra[i][0]**2 / 12
                Nodos[2*i+1]= -Barra[i][6]*Barra[i][0]**2 / 12
    
                
            elif Barra[i][5]==2: # Emp- art: M=ql^2/8
                Nodos[2*i+1]= 0
                Nodos[2*i]= Barra[i][6]*Barra[i][0]**2 / 8
                
            elif Barra[i][5]==3:  # Emp:libre: M=ql^2/2
                Nodos[2*i+1]= 0
                Nodos[2*i]= Barra[i][6]*Barra[i][0]**2 / 2
        else: #Barras intermedias
        
            if Barra[i][5]==1: # emp-emp: ql^2/12
                Nodos[2*i]= Barra[i][6]*Barra[i][0]**2 / 12
                Nodos[2*i+1]= -Barra[i][6]*Barra[i][0]**2 / 12


MomEmpPerf(Barra)           #Momento de empotramiento Perfecto 

for i in range(len(Barra)):
    print(Barra[i])

MetCross(Barra)            #Metodo de Cross

