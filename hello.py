#!/usr/bin/env python3
# SHEBANG acima
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "LúcioFdaSilva"
__license__ = "Unlicense"
# Dunder

import os


# Este programa imprime Hello, World!
#if __name__ == "__main__":
#    print("Hello, World!")
#    print("Lúcio".upper())


current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == 'pt_BR':
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)
print("Lúcio".upper())

#POSSO EXECUTAR ASSIM, passando a variável de ambiente
#LANG=it_IT python3 hello.py

#Usando ambientes virtuais
#É possivel criar uma cópia do:

#which python
#Mostra onde o python está instalado

#python3 -m site
#Mostra onde estão localizados os arquivos, pacotes e o interpretador python

#Exclusiva para uma aplicação

#Como criar um ambiente virtual?
#python3 -m venv .venv

#Como ativar um ambiente virtual?
#source .venv/bin/activate

