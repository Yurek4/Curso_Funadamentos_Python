list1 = ["Maça","Banana", "Cacau","Amora"] #Criando uma lista de frutas
list2 = ["2","3","4","5"] #Criando uma lista de numeros
list3 = [True, False, True] #Criando uma lista com valores boleanas

print(list1) #Exibindo a lista1 
print(list2) #Exibindo a lista2
print(list3) #Exibindo a lista3


print(len(list1)) # "len" ele conta a quantidade de itens que tem dentro de uma lista

list4 = ["abc", 34, True, 40, "mais"] # uma lista mista com numero strings, valores boleanos e números

print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))
print("Se parando o código")
thislist = list(("apple","banana","melon"))
print(thislist)#Printando a lista 
print(thislist[1])#Pritando o indice um da lista que é a banana 
print(thislist[-1])#Printando o melon, pois quando vc define o indice ele vai percorrer a lista e indo para o ultmo

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5]) #: A pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).
