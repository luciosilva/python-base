#!/usr/bin/env python3
"""
#numbers = [1,2,3,4,5,6]

numbers = range(1,700000,1)#start, next, stop

print(numbers[-1])
print(numbers[2:])

#Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue
#       break    
    print(f"mais codigo com {number}")
"""
dados = {}

# For loops / Laço for
for line in open("post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()
print(dados)

original = [1,2,3]

# For loops / Laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List Comprehension sempre cria uma nova lista
dobrada = [n*2 for n in original]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt") 
    if ":" in line
}
print(dados)

dados  = {}
for line in open("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()
print(dados)

