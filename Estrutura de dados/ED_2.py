class Stack:
    def __init__(self): #Todas as classes têm uma função chamada __init__(), 
                        #que é sempre executada quando a classe está sendo iniciada
        self.stack = [] #Criando a pilha
    #O self parâmetro é uma referência à instância 
    #atual da classe e é usado para acessar variáveis ​​que pertencem à classe.
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    # Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())