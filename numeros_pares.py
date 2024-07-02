#!/usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python numeros_pares.py`
2
4
6
8
...
"""
numeros = range(1,201)

for numero in numeros:
    if numero %2 != 0:
        continue
    print(numero)

[print(n) for n in numeros if n %2 == 0]