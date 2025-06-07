Lista1 = ["Agua", "fermento","chá","arroz","feijão","Açucar","macarrão"] #Lista de coisas 

for x in Lista1: #Loop que percorre toda lista e printa todos os itens
   print(x)

lista2 = ["Agua", "fermento","chá","arroz","feijão","Açucar","macarrão"]

for i in range(len(lista2)):
   print(lista2[i])


lista3 = ["Agua", "fermento","chá","arroz","feijão","Açucar","macarrão"]
y = 0

while y < len(lista3): #Use a len()função para determinar o comprimento da lista, comece em 0 e percorra os itens da lista consultando seus índices.
    print(lista3[y])
    y = y + 1
    
