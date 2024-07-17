from random import choice
import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

logo='''      _                         _         _____                   
     | | ___   __ _  ___     __| | __ _  |  ___|__  _ __ ___ __ _ 
  _  | |/ _ \\ / _` |/ _ \\   / _` |/ _` | | |_ / _ \\| '__/ __/ _` |
 | |_| | (_) | (_| | (_) | | (_| | (_| | |  _| (_) | | | (_| (_| |
  \\___/ \\___/ \\__, |\\___/   \\__,_|\\__,_| |_|  \\___/|_|  \\___\\__,_|
              |___/                                               '''

animais = ('formiga babuino texugo morcego urso castor camelo gato molusco cobra puma '
           'coiote corvo veado cachorro burro pato aguia furao raposa sapo cabra '
           'ganso falcao leao lagarto lhama macaco toupeira alce rato mula tritao '
           'lontra coruja panda papagaio pombo coelho carneiro rato corvo '
           'rinoceronte salmao foca tubarao ovelha gamba preguiça cobra aranha '
           'cegonha cisne tigre sapo truta peru tartaruga doninha baleia lobo '
           'zebra ').split()
palavra_secreta = choice(animais)
palavra_adivinhada1 = []
letras_digitadas=[]
letras_digitadas_formatadas=()
for letra in palavra_secreta:
    palavra_adivinhada1.append('_')
numero_acertos = 0
numero_erros = 0
desenhos_forca = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
while True:
    print(logo)
    if numero_acertos>0 or numero_erros>0:
        print(f'\nLetras digitadas: {letras_digitadas_formatadas}')
    print(desenhos_forca[numero_erros])
    palavra_adivinhada2= ' '.join(palavra_adivinhada1)
    print(f'\n{palavra_adivinhada2}')
    letra_digitada = input('\nDigite uma letra:\n')
    letras_digitadas.append(letra_digitada)
    letras_digitadas_formatadas='-'.join(letras_digitadas)
    limpar_terminal()
    for posicao, letra in enumerate(palavra_secreta):
        if letra_digitada == letra:
            palavra_adivinhada1.insert(posicao, letra_digitada)
            palavra_adivinhada1.pop(posicao + 1)
            numero_acertos += 1
    if letra_digitada not in palavra_secreta:
        numero_erros += 1
    if numero_acertos == len(palavra_secreta):
        limpar_terminal()
        print(logo)
        if numero_acertos>0 or numero_erros>0:
            print(f'\nLetras digitadas: {letras_digitadas_formatadas}')
        print(desenhos_forca[numero_erros])
        print('\nVocê venceu!')
        break
    elif numero_erros == len(desenhos_forca) - 1:
        limpar_terminal()
        print(logo)
        if numero_acertos>0 or numero_erros>0:
            print(f'\nLetras digitadas: {letras_digitadas_formatadas}')
        print(desenhos_forca[numero_erros])
        print('\nVocê perdeu :(')
        break
print(f'\nA palavra era: {palavra_secreta}')
