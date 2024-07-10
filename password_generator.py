from random import randint, shuffle
alfabeto=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
simbolos=['!', '@', '#', '$', '%', '&', '*', '?']
numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_letras=int(input('Quantas letras você quer na sua senha?\n'))
num_simbolos=int(input('Quantos símbolos você quer na sua senha?\n'))
num_numeros=int(input('Quantos números você quer na sua senha?\n'))
senha_lista=list()
senha=None
if num_letras>0:
    for a in range(0,num_letras):
        senha_lista.append(alfabeto[randint(0,len(alfabeto)-1)])
if num_simbolos>0:
    for a in range(0, num_simbolos):
        senha_lista.append(simbolos[randint(0,len(simbolos)-1)])
if num_numeros>0:
    for a in range(0,num_numeros):
        senha_lista.append(numeros[randint(0,len(numeros)-1)])
shuffle(senha_lista)
senha=''.join(senha_lista)
print(f'Sua nova senha é: {senha}')
