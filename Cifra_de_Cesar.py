import string
def codificar_decodificar(frase,modulo): 
    while modulo>26:
        modulo-=26   
    num=0
    while num!=modulo:
        for i in range(modulo,len(alfabeto)):
            alfabeto_codificado.append(alfabeto[i])
        while num!=modulo:
            alfabeto_codificado.append(alfabeto[num])
            num+=1
    for letra in frase:
        if letra.isalpha():
            if n1==1:
                frase_codificada.append(alfabeto_codificado[alfabeto.index(letra)])
            elif n1==2:
                frase_codificada.append(alfabeto[alfabeto_codificado.index(letra)])
        elif letra.isspace():
            frase_codificada.append(' ')
        elif letra in string.punctuation:
            frase_codificada.append(letra)
        else:
            continue
while True:
    n1=float('inf')
    alfabeto=string.ascii_lowercase
    alfabeto_codificado=[]
    frase_codificada=[]
    while n1>2 or n1<0:
        n1=int(input('Digite 1 para codificar, e 2 para decodificar(0 para sair):\n'))
    if n1==0:
        break
    frase_usuario=input('digite a frase:\n').lower().strip()
    funçao=int(input('digite a função:\n'))
    codificar_decodificar(frase=frase_usuario,modulo=funçao)
    frase_codificada_ajeitada=''.join(frase_codificada)
    print(f'Sua frase ficou assim:\n{frase_codificada_ajeitada}')
