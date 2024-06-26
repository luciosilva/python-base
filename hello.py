#!/usr/bin/env python3
# SHEBANG acima
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR
    Ou informe através do CLI argument `--lang`
    Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "LúcioFdaSilva"
__license__ = "Unlicense"
# Dunder, nos objetos chamam de protocolos

import os
import sys

#print(sys.argv)

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
#    print(f"{args}")
#    print(args.split("="))
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value =  value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
#    print(key, value)
    arguments[key] = value

# Este programa imprime Hello, World!
#if __name__ == "__main__":
#    print("Hello, World!")
#    print("Lúcio".upper())

current_language = arguments["lang"]
if current_language is None:
    #TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else: current_language = input("Choose a language:")
    
current_language = current_language[:5]
    
    
#LANG=pt_BR ipython hello.py 
msg = {
    "C.UTF": "Hello, World!", 
    "en_US": "Hello, World!", 
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, mondo!",
    "es_SP": "Hola, mundo!",
    "fr_FR": "Bonjour monde!"
    }

print(msg[current_language] * int(arguments["count"]))
print("Lúcio".upper())

#POSSO EXECUTAR ASSIM, passando a variável de ambiente
#LANG=it_IT python3 hello.py

#Usando ambientes virtuais
#É possivel criar uma cópia do:

#Mostra onde o python está instalado
#which python

#Mostra onde estão localizados os arquivos, pacotes e o interpretador python
#python3 -m site

#Exclusiva para uma aplicação

#Como criar um ambiente virtual?
#python3 -m venv .venv

#Como ativar um ambiente virtual?
#source .venv/bin/activate

#python -m pip --help
#python -m pip install ipython
#python -m pip install --upgrade pip
#Novo interpretador, colorido, auto complete e help melhorado
#ipython

#Help - mostra todos os módulos
#import os
#Help - mostra o help do getenv
#os.getenv?
#Help - mostra o código do getenv
#os.getenv??

#Mostra o tempo para execução do print
#%time print("a")

#TIPOS
#Retorna os binários
#bin()
#Endereço de memória
#id()
#Scalar types - Tipos primários

#Ver caracteristicas das classes
#dir(int)

#Para dinheiro não usar float, usar decimal ou currency




