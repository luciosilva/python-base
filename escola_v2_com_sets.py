#!/usr/bin/env python3


#c1 = {1, 2, 3}
#type(c1)
##tipo:set

##Sempre que possível criar assim
#c1 = set()
#c1 = set((1,2,3))

#c1 = set("banana")
#c1 = {'a', 'b', 'n'}

#conjunto_a = {1, 2, 3, 4, 5}
#conjunto_b = {4, 5, 6, 7, 8}

#set(conjunto_a) | set(conjunto_b)
#set(conjunto_a).union(set(conjunto_b))
#{1,2,3,4,5,6,7,8}

#set(conjunto_a).intersection(set(conjunto_b))
#set(conjunto_a) & (set(conjunto_b))

##diference
#conjunto_a.difference(conjunto_b)
#conjunto_a - conjunto_b

##Diferença simétrica(todos os elementos só do conjuto A e não no B)
#conjunto_a.symmetric_difference(conjunto_b)
#conjunto_a ^ conjunto_b


#União
#conjunto_a | conjunto_b
#{1, 2, 3, 4, 5, 6, 7, 8}

#Intersec
#conjunto_a & conjunto_b
#{4, 5}

#conjunto_a - conjunto_b
#{1, 2, 4}

#conjunto_a ^ conjunto_b
#{1, 2, 3, 4, 5, 6, 7, 8}


#Set - conjunto
#Implementa um hash_table quep otimiza as buscas
#Buscas otimizadas
#Não permite ordenação
#Não tem como pegar com indice


"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequenta cada uma das atividades.
"""

__version__ = "0.1.1"

#Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]



aula_ingles = ["Erik", "Maia","Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica),
    ("Dança", aula_danca),
]


for nome_atividade, atividade in atividades:
    
    print(f"Alunos da atividade {nome_atividade}")
    #Listar alunos em cada atividade por sala
    atividade_sala1 = []
    atividade_sala2 = []

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("Sala 1 ", atividade_sala1)
    print("Sala 2 ", atividade_sala2)

    print()
    print("#" * 40)