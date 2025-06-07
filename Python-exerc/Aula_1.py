#Primeiro programa
#Autor:Yuri 
#Rotina de entrada

nome = input("Qual é o seu nome? ") #nome é uma variavel string
idade = int(input("Quantos anos vc tem ? ")) #idade é uma variavel tipo inteira
altura = float(input("Qual é a sua altura em metros? ")) #altura é uma variavel tipo float


#Processando informações
ano_nascimento = 2025 - idade #calcula o ano de nascimento

#Imprimir os dados
print(f"\n Olá, {nome}") #Exibir uma saudação!
print(f"Você nasceu em {ano_nascimento}")#exibir o ano de nascimento
print(f"Sua altura é {altura:.2f}")#exibir altura com 2 casas decimais
print("Vamos calcular o seu IMC!") #Mensagem para o usuário

def imc(): #Criando a função imc
    peso = float(input("Qual é o seu peso em kg?")) # Pedindo o peso do usuário
    imc_calc = peso / (altura ** 2 ) #Calcular o imc
    print(f"Seu imc é {imc_calc:.4}")#exibir o imc com 2 casas decimais 
    return imc_calc #retorna o valor do imc

imc() #chama a função imc