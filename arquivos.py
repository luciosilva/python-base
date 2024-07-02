#!/usr/bin/env python3
import os

#Lista o conteúdo da pasta atual
os.listdir(".")

#cria pasta
os.mkdir("pasta1")

os.makedirs("pasta1/subpasta", exist_ok=True)

#Resolve a \ ou a /
path - os.path.join("pasta","subpasta")

os.makedirs(path, exist_ok=True)

#Retorna o diretório atual
os.curdir

os.listdir(os.curdir)

#Igual ao touch, cria arquivo vazio
os.mknod(os.path.join(path,"arquivo.txt"))
os.listdir(path)

#Começando a preparar a escrita no arquivo
filepath = os.path.join(path, "arquivo.txt")

#Retorna o nome do arquivo
os.path.basename(filepath)

#Se o arquivo existe True or False
os.path.exists(filepath)

#Retorna o caminho absoluto
os.path.abspath(path)

#Padrão é read
arquivo = open(filepath)

#Padrão é read
arquivo = open(filepath, "r")

arquivo.read()

#Para escrever usar o w
arquivo = open(filepath, "w")
arquivo.write("Bruno\n")
arquivo.close()

open(filepath).read()

#Modo de append
arquivo = open(filepath, "a")

#Context manager
with open(filepath, "w") as arquivo:
    arquivo.write("Hello\n")
    arquivo.write("World\n")

open(filepath).read()


print("Brasil", file=open(filepath, "a"))
print(open(filepath).read())

text = [
    "Titulo\n",
    "\n",
    "Este post fala sobre \n",
    "o assunto bla bla bla\n",
]

filepath = os.path.join(path, "texto.txt")

with open(filepath, "a") as arquivo:
        arquivo.writelines(text)

print(open(filepath).read())
open(filepath).readlines()


from pathlib import Path

path = Path("pasta") / Path("subpasta")

(path / "outrapasta").mkdir()

filepath = Path("pasta") / "teste1.txt"

filepath.write_text("Hello")
filepath.open("w")
filepath.read_text()
