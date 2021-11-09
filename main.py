#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Código para resolver um sistema linear
        A*x = b
sendo A uma matrix m por m e b uma matriz m por 1.

Os dados das matrizes são passados por arquivo CSV.

Nota: foi projetado para ler os dados de um arquivo chamado
'data.csv' localizado no mesmo diretório do código.

Considerando que a matriz A é m por m e que o sistema tem solução única, então a matriz é invertível e a solução é dada pré-multiplicando pela inversa de A
         inv(A)@A@x = inv(A)@b
    ===> I@x = inv(A)@b
    ===> x = inv(A)@b
"""

# Bibliotecas
import numpy as np
from numpy.linalg import inv

# Importar CSV
A_amp = np.genfromtxt('data.csv', delimiter=',')

#
AA = A_amp[:A_amp.shape[0],:A_amp.shape[0]]
bb = A_amp[:,-1].reshape((len(AA),1))

xx = inv(AA)@bb

print('Seja o sistema:')
for i in range(A_amp.shape[0]):
    print('\t',end='')
    for j in range(A_amp.shape[1]-1):
        if A_amp[i,j] > 0:
            print(f'+ {A_amp[i,j]}*x{j+1} ',end='')
        else:
            print(f'- {abs(A_amp[i,j])}*x{j+1} ',end='')
    print(f'= {A_amp[i,j+1]}')

print('A sua solução do sistema:')
for i, x in enumerate(xx):
    print(f'\tx{i+1} = {x[0]}')
