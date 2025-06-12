stack = []
#Push adicionando um novo elemento na lista
stack.append("A")
stack.append("B")
stack.append("c")

#printando a lista
print(stack)
#peek retorna o elemento superior (ultimo) na pilha
topElemtent = stack[-1]
print("Peek", topElemtent)
#pop remove e retorna o elemento do topo da pilha
poppedElement = stack.pop()
print("Pop", poppedElement)

#Stack after Pop
print("Stack after Pop",stack)
#Verifica se a pilha está vazia
isEmpty = not bool(stack)
print("isEmpty",isEmpty)

#Size
print("Size: ", len(stack))