import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import math as mt
diccionario = {'M':1, 'M':1, 'M':1 , 'N':1 ,  'M':1 ,'M':1 , 'M':1 , 'N':1, 'M':1 , 'M':1 , 'M':1 , 'N':1 , 'P':1 , 'P':1 , 'P':1 , 'B':1}
valores = diccionario.values()
letras = diccionario.keys()
letras.sort()
fig = plt.figure(figsize=(4,4))
for i in range(1,17):
    ax = fig.add_subplot(4, 4, i, xticklabels=[], yticklabels=[], xticks=[], yticks=[])  
plt.savefig("Terreno_vacio.png")
plt.show()
fig2 = plt.figure(figsize=(4,4))
for i in range(1,17):
    ax = fig2.add_subplot(4, 4,i, xticklabels=[], yticklabels=[], xticks=[], yticks=[])  
    plt.text(0.2, 0.4,letras[i%4])
plt.savefig("Terreno_Con_Letras.png")
plt.show()