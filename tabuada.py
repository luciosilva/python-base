#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.1"
__author__ = "Bruno"


template = """

{bloco}    

##################
"""


#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# Iterable (percorriveis)


# para cada numero em numeros:
#for numero in numeros:
#    print("Tabuada do:", numero)
#    for outro_numero in numeros:
#        print(numero * outro_numero)
#    print('-' * 30)
#print(numeros)


#MEU
#for n1 in numeros:
#    print("{:-^18}".format("Tabuada do {n1}"))
#    bloco = ""
#    for n2 in numeros:
#        resultado = n1 * n2
#        bloco +=  f"{'': <4} {n1} x {n2} = {resultado}\n"
#    print(template.format(bloco=bloco))


#BRUNO
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)



#fruit = "melancia"
#fruit_encode = fruit.encode("utf-8")
#fruit_decode = fruit.decode("utf-8")


#nome = "Bruno"
#bytes(nome, "utf-8")
#type(bytes(nome, "utf-8"))
#list(bytes(nome, "utf-8"))

#"Lucio " * 3
#for letra in nome:
#        print("--> ", letra)


#iter_nome = nome.__iter__()

#next(iter_nome)
