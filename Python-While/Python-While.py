import time


i = 1 

while i < 6: #Loop de enquanto "i" for menor que 6 ele vai imprimir o valor de "i" 
    print(i)
    time.sleep(3)
    if i == 3: # Esse "if" usado com o break é para interromper o loop pela metade
        break   #
    i +=1 #Aqui é uma sistema de acumulação, sempre adicionando 1 
