#1– Crie um programa que receba um número. Se o número for maior que  1000 o programa deve dividi-lo por 50.
# Se o número for menor ou igual a 1000 o programa deve  elevá-lo à potência 2
#Inicio do programa     
numero = float(input("Digite um numero: ")) #Pedindo o numero do tipo float 

if numero > 1000: #terminando a condição se o numero é maior que 100
    numero_dividido = numero/50 #dividio o numero por 50
    print(f"O valor do seu numero divido por 50 é {numero_dividido}")#exibindo para o user o valor do numero divido
else:#COntra condição   
    numero_ao_quadrado = numero**2# elevando o numero ao quadrado
    print(f"O valor do seu numero elevado ao quadrado é {numero_ao_quadrado}")#exibindo para o user o numero dele ao quadrado