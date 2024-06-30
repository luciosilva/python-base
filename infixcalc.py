#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalv.py sum 5 2
7

$ infixcalv.py mul 10 5
50

$ infixcalv.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__="0.1.0"
__author__ = "LúcioFdaSilva"
__license__ = "Unlicense"
# Dunder, nos objetos chamam de protocolos

import sys
import os
from datetime import datetime
import logging

log_level = os.getenv("LOG_LEVEL", "WARING").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


"""
arguments = {
    "oper": None,
    "num1": None,
    "num2": None,
}

valid_operations = ["sum", "sub", "mul", "div"]

operation = ""
num1 = 0
num2 = 0

if len(sys.argv) > 1:
    if len(sys.argv) != 4:
        print("São esperados 0 ou 3 argumentos")
        sys.exit(1)
    if sys.argv[1] not in valid_operations:
        print("As operações permitidas são: sum, sub, mul e div")
        sys.exit(1)
    if not sys.argv[2].isdigit() or not sys.argv[3].isdigit():
        print("Os valores tem que ser numéricos")
        sys.exit(1)
        
    operation = sys.argv[1]
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])
    
else:
    operation = input('operação:')
    num1 = int(input('n1:'))
    num2 = int(input('n2:'))    

if operation == "sum":
    print(num1 + num2)

if operation == "sub":
    print(num1 - num2)

if operation == "mul":
    print(num1 * num2)

if operation == "div":
    print(num1 / num2)
    
"""
    
arguments = sys.argv[1:]
# Validação
if not arguments:
    operation = input("operação:")
    n1 + input("n1:")
    n2 + input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:

    if not num.replace(".","").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)    

if operation == "sum":
    result = n1 + n2 

if operation == "sub":
    result = n1 - n2

if operation == "mul":
    result = n1 * n2

if operation == "div":
    try:
        result = n1 / n2
    except ZeroDivisionError as e:
        print(str(e))
        sys.exit(1)
        

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

print(f"O resultado é {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
#    print(f"{operation},{n1},{n2} = {result}\n", file=open(filename, "a"))
except PermissionError as e:
    log.error(
        "msg: %s",
        str(e)
    )    
    sys.exit(1)