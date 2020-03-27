#-*-coding: utf-8-*-
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import math as mt
#Creación diccionario
diccionario = {'P(01,M),':1, 'P(02,M)':0, 'P(03,P)':1 , 'P(04,P)':0 ,'P(05,N)':1 ,'P(06,N)':0 , 'P(07,M)':1 , 'P(08,P)':1, 'P(09,S)':1 , 'P(10,M)':0 , 'P(11,S)':0 , 'P(12,B)':1 , 'P(13,B)':1 , 'P(14,M)':1 , 'P(15,P)':1 , 'P(16,M)':0}
#Aqui se accede a los valores del diccionario
valores = diccionario.values()
#Aqui se accede a las llaves del diccionario
letras = diccionario.keys()
letras.sort()
#Se pasa letras de lista a matriz y además se tranpone para que asi quede el orden que queremos para el proyecto
w = 4
c = [[0 for x in range(w)] for y in range(w)]
for i in range(0,4):
    for j in range(0,4):
        c[i][j] = letras[i*(4)+j] 
c2 = np.array(c)
tras = c2.transpose()
#Creamos el primer terreno de 4x4, este terreno esta vacio. Además se guarda la imagen
fig = plt.figure(figsize=(4,4))
for i in range(1,17):
    ax = fig.add_subplot(4, 4, i, xticklabels=[], yticklabels=[], xticks=[], yticks=[])  
plt.savefig("Terreno_vacio.png")
plt.show()
#Se crea el terreno de 4x4 con las modificaciones de que segun el valor sea 1 o 0 cada componente tendra o no un elemento
fig2 = plt.figure(figsize=(4,4))
k = 1
for i in range(1,5):
    for j in range(1,5):
        if diccionario.get(tras[i-1][j-1])==1:
            ax = fig2.add_subplot(4, 4,k, xticklabels=[], yticklabels=[], xticks=[], yticks=[])  
            plt.text(0.2, 0.4,tras[i-1][j-1])
        elif diccionario.get(tras[i-1][j-1]) == 0:
            ax = fig2.add_subplot(4, 4,k, xticklabels=[], yticklabels=[], xticks=[], yticks=[])  
            plt.text(0.2, 0.4,' ')
        k += 1
plt.savefig("Terreno_Con_Letras.png")
plt.show()