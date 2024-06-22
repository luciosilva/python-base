pontos = 2, 1, 99

x, y, z = pontos

#unpacking, spread, explode

x, *_ = pontos
#x=2
#-=[1, 99]

head, *body, tail = pontos

pontos[0]
pontos.count(2)
pontos[2:]
pontos[:2]
pontos[1:2]
len(pontos)
