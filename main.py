import numpy as np
import random
import matplotlib.pyplot as plt
import math as math
from celluloid import Camera
x=[]
y=[]
x_1=[]
y_1=[]
dim = 20
a = np.zeros((dim, dim))
vecinosX=[]
vecinosY=[]
sinVecinosX=[]
sinVecinosY=[]
numeroFilasMatriz=a.shape[0];
dimColumnasMatriz=a.shape[1];

def crearCoordenadas(numeroCoordenadas):
    for _ in range(numeroCoordenadas):
        n1 = random.randint(0,19)
        n2 = random.randint(0,19)
        x.append(n1)
        y.append(n2)

def insertarCoordenadas(x,y):
    for i in range(len(x)):
        a[x[i],y[i]]=1;

def detectaVecinos(x_1, y_1, indice, arregloEnteros1, arregloEnteros2):

    for i in arregloEnteros1:
        for j in arregloEnteros2:
            try:
                if(i==0 and j==0):
                    continue;
                if(a[x_1[indice]+i,y_1[indice]+j]==1):
                    vecinosX.append(x_1[indice]+i)
                    vecinosY.append(y_1[indice]+j)
                else:
                    sinVecinosX.append(x_1[indice])
                    sinVecinosY.append(y_1[indice])
            except:
                print(f'a[{x_1[indice]},{y_1[indice]}] en el perimetro de la matriz')
                print("Por el momento no se dibujara, posteriormente se incorporara la solucion del presente error")

crearCoordenadas(10)
insertarCoordenadas(x,y)




for i in range(numeroFilasMatriz):
    for j in range(dimColumnasMatriz):
        if (a[i,j]==1):
            x_1.append(i)
            y_1.append(j)

dimCeldas1=len(x_1)
arregloEnteros1 = [*range(-1, 1 + 1, 1)]
arregloEnteros2 = [*range(-1, 1 + 1, 1)]


for indice in range(dimCeldas1):

    detectaVecinos(x_1, y_1, indice, arregloEnteros1, arregloEnteros2)

plt.plot(sinVecinosY, sinVecinosX, 'om') #plot (y,x , tipo de modelo)
plt.plot(vecinosY,vecinosX,'go')
plt.show()

