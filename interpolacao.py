#!/usr/bin/env python3

nome.upper()
nome.lower()
"bruno rocha".capitalize()
"bruno rocha".title()
"bruno rocha".split()
"bruno rocha".startswith("B")
"bruno rocha".upper().startswith("b")
"bruno rocha".upper().endswith("b")

sorted("bruno rocha")
list(reversed("bruno rocha"))


#nome = "Bruno"
#saldo = 30.0
#python só concatena strings
#print("O saldo do " + nome + " é total de " + string(saldo))

#interpolação
#template = "O saldo do %s é o total de %f"
#template % (nome, saldo)

#"Olá, %s" % "Bruno"
#"Olá, %s" % 1234

#msg = "Olá, %s você é o player n %03d e você tem %.2f pontos"
#msg % ("Bruno", 2, 987.3)










email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f

"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl % {
            "nome": cliente, 
            "produto": "caneta", 
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )
    
    
str.format
msg = "Olá, %s você é o player n %03d e você tem %.2f pontos"
msg % ("Bruno", 2, 987.3)

msg = "Olá, {} você é o player n {:03d} e você tem {:.3f} pontos"
msg.format("Bruno", 2, 987.3)

"{}".format("Bruno")
"{:^11}".format("Bruno")
"{:<11}".format("Bruno")
"{:>11}".format("Bruno")
"{:-^11}".format("Bruno")
"{:-^11.3}".format("Bruno")
#Fica estranho
"{:-^11.3}".format(456.89)

"{:.2f}".format(456.89)

"{:^20.4f}".format(456.89)

msg = "Olá, {nome} você é o player n {num:03d} e você tem {pont:.3f} pontos"
msg.format(nome="Bruno", num=2, pont=987.3)

#f-strings


nome = "Joao"
saldo = 89

f"Olá, {nome} você tem {saldo:.2f}"

# Concatenação %self.
# quando usar a biblioteca logging

#str.format{}
#mensagens longas, e-mail

# f-strngs
#restantes, msg, print, error

print("\U0001F43C")
print("\N{panda face}")
print("\N{green apple}")
print("\N{party popper}")
