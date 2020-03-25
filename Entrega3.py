import matplotlib.pyplot as plt
from pylab import *
import numpy as np
diccionario = {'Q1':1, 'Q2':0, 'Q3':1 , 'Q4':0 ,  'P1':1 ,'P2':0 , 'P3':1 , 'P4':1, 'R1':1 , 'R2':0 , 'R3':0 , 'R4':1 , 'S1':1 , 'S2':1 , 'S3':1 , 'S4':0}
valores = diccionario.values()
letras = diccionario.keys()
fig = plt.figure(figsize=(4,4))
for i in range(1,17):
    ax = fig.add_subplot(4, 4, i, xticklabels=[], yticklabels=[], xticks=[], yticks=[])
    
plt.savefig("Terreno_vacio.png")
plt.show()
