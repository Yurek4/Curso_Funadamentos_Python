#3. Crie um programa em Python que calcule o perímetro de uma circunferência e exiba o valor arredondado com duas casas decimais. 
# perimetro_circ = 2 * π * raio 

#Inicio do programa
raio = float(input("Digite o raio do circulo "))# Pedindo o raio do circulo 


def perimetro_circulo(raio):#Criando a funçãoq que calcula o perimetro do circulo 
    pi = 3.14
    perimetro = 2 * pi * raio # Calculando o perimetro do circulo
    print(f"O  raio é {raio}")#Printando o raio do circulo na tela
    print(f"O pericmetro do circulo é {perimetro:.4}")#Printar o perimetro do circulo com 2 casas decimais
    return perimetro # Retornando o perimetro do circulo para o programa principal

perimetro_circulo(raio) #Chamando a função que calcula o perimetro do circulo

#4. Crie um programa em Python que calcule a área de uma circunferência e exiba o valor arredondado com duas casas decimais.
# area_circ = π * raio² 

def area_circulo(raio): # Criando a função que calcula a área do circulo
    pi = 3.14 # Definindo o valor de pi
    area = pi * (raio**2)#Calculando a área do circulo
    print(f"A área do circulo é {area:.2f}")#Printando a área do circulo com 2 casas decimais
    return area # retornando a área do circulo para o programa principal 
area_circulo(raio)#Puxando a função que calcula a área do circulo