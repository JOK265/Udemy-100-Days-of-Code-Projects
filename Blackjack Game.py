from random import choice

cartas_usuario = []
cartas_computador = []


def cartas_sorteadas():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta = choice(cartas)
    return carta

def somar_cartas():
    global soma_usuario, soma_computador
    soma_usuario = sum(cartas_usuario)
    soma_computador = sum(cartas_computador)
    return soma_usuario, soma_computador

def pegar_uma_carta():
    while True:
        n1 = input(f'Suas cartas são: {cartas_usuario}\nA primeira carta do computador é: {cartas_computador[0]}\nDeseja pegar mais uma carta?[S/N]\n').lower()
        if n1=='s':
            cartas_usuario.append(cartas_sorteadas())
            cartas_computador.append(cartas_sorteadas())
            somar_cartas()
            if soma_usuario>=21 or soma_computador>=21:
                if 11 in cartas_usuario:
                    cartas_usuario[cartas_usuario.index(11)] = 1
                if 11 in cartas_computador:
                    cartas_computador[cartas_computador.index(11)] = 1
                somar_cartas()
                if soma_usuario>=21 or soma_computador>=21:
                    break
        else:
            break

for i in range(2):
    cartas_usuario.append(cartas_sorteadas())
    cartas_computador.append(cartas_sorteadas())

pegar_uma_carta()

if soma_usuario==soma_computador:
    print('Temos um empate :/')
elif soma_computador>21 or soma_usuario<=21 and soma_usuario>soma_computador:
    print('Você venceu!!')
elif soma_usuario>21 or soma_computador<=21 and soma_computador>soma_usuario:
    print('Você perdeu :(')

print(f'Suas cartas foram: {cartas_usuario}\nVocê somou um total de {final_soma_usuario} pontos\nJá as cartas do computador foram: {cartas_computador}\nQue somaram um total de {soma_computador} pontos')
