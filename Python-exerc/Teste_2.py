a = int(input("Digite o primeiro número: ")) #INSERINDO O PRIMEIRO NÚMERO INTEIRO 
b = int(input("Digite o segundo número: ")) #INSERENDO O SEGUNDO NÚMERO INTEIRO

def somatoria():    #FUNÇÃO SOMATIVA QUE PEGA "a" E "b" E RETORNA A SOMA
    
    soma = a + b 
    return soma

somatoria() #CHAMANDO A FUNÇÃO SOMATIVA

print("A soma é:", somatoria()) #IMPRIMINDO O RESULTADO DA FUNÇÃO SOMATIVA
