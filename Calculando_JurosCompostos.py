#Inicio do programa
#Calcular o valor do juros compostos: Desenvolva uma função que calcule o valor final de 
#um investimento com base em uma taxa de juros e um período de tempo.

capital_inicial = int(input("Digite o valor do Capital inicial de aplicação: ")) # Pedindo o Capital inicial do type float
taxa_juros = float(input("Digite o valor da taxa de juros(Em porcentagem): ")) # Pedindo o valor da taxas em juros em porcentagem
tempo_da_aplicacao = int(input("Digite o tempo que vai se a aplicação (tempo em anos): ")) # Pedindo o tempo em anos type int

def calculo_juros (capital_inicial, taxa_juros, tempo_de_aplicacao): # Criei uma função que calcula o juros composto e pega 3 variaveis externa 
    i = taxa_juros /100  #Transformando a porcentagem da taxa de juros em porcentagem
    montante_final = capital_inicial * (1 + i)**tempo_da_aplicacao #Calculando o montante final
    juros_acumulado = montante_final - capital_inicial #Calculo do juros acumulado
    print(f"O valor do juros acumulado em {tempo_da_aplicacao} anos é de {juros_acumulado:.4} : ") #Printando tudo 
    

calculo_juros(capital_inicial,taxa_juros,tempo_da_aplicacao) #Chamando a função calculando juros
