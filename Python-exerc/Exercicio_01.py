#Crie um programa em Python que solicite o valor da base e altura e calcule a área de um retângulo,
#apresentando no final todos os valores na tela. area_retangulo = base x altura 
#Inicio do programa
base = float(input("Digite a base do triangulo: "))  # INSERINDO A BASE DO TRIÂNGULO
altura = float(input("Digite a altura do triangulo: "))  # INSERINDO A ALTURA DO TRIÂNGULO

#Criando uma função para calcular a área do triangulo
def area_triangulo(base, altura): # Aqui eu puxo as duas vairaveis base e altura para a função
    area = (base*altura) / 2 # Calculando a área do triangulo
    print(f"A Área do traingulo é {area:.2f}")# Mostrando a area do triangulo com 2 casas decimais
    return area # Voltando a araea do triangulo para o programa principal
print(f"A base do triangulo é {base}")#Exibindo a base do triangulo
print(f"Altura do triangulo é {altura}")#exibindo a altura do triangulo 
area_triangulo(base, altura)
