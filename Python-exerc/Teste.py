

print("inicio do programa")
nota1 = int(input("digite a sua primeira nota (De zero a dez): ")) 
nota2 = int(input("digite a sua segunda nota(De zero a dez): ")) 
nota3 = int(input("digite a sua terceira nota(De zero a dez): ")) 

media = (nota1+nota2+nota3)/3

if media >= 7:
    print("Aprovado")   
else:
    print("Reprovado")
print("Fim do programa")
print("A média é: ", media)
