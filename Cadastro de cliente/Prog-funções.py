#Lista global que irá armazenar todos os clientes cadastrados 
clientes = []
#função para cadastrar um novo cliente

def cadastra_cliente():
    nome = input("Digite o nome do cliente: ") # Pedindo o nome do cliente formato string
    idade = int(input("Digite a idade do clieten: ")) # Pedindo a idade do cliente formato inteiro
    cidade = input("Digite a cidade do cliente:") # Pedidno a cidade do cliente formato string
    

    # Criar um dicionario representando o cliente

    cliente = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "compras": []# lista que armaazenara tupla de compras(Produto, valor)
    
    }
    #adidcionar o cliente a lista global
    clientes.append(cliente)
    #retorna o cliente criado 
    return cliente

#função para registrar uma compra de um cliente
def registrar_compra(cliente):
    try:
        #solicita o nome do produto comprado
        produto = input("Digite o nome do produto comprado: ")
        
        #solicita o valor do produto e converte para float
        valor = float(input("Dgigite o valor do produto: R$ "))
        
        #criar um tupla com o (produto, valor) e adiciona na lista do cliente
        cliente["compras"].append((produto, valor))
        
        #confirmação visual 
        print(f"Compra registrada: {produto} - R$ {valor:.4f}")
    except ValueError:
        # Caso o user digite um valor inválido
        print("Erro: Valor inválido. Por favor, digite um número válido para o valor do produto.")
        
#Função para calcular o total gasto por um cliente
def calcular_total_gasto(cliente):
    #soma de todas as compras feitas pelo cliente
    total = sum(valor for _, valor in cliente["compras"])
    #retornar o total calculado
    return total

#Funçao o para listar todos os cliente cadastrados e suas informação 
def  listar_clientes():
    #verificar se ha clientes cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado ainda.")
        return
    #Percorre cada cliente na lista de clientes
    for cliente in clientes:
        #Calacular o total gasto pelo cliente usando uma funça com retorno
        total = calcular_total_gasto(cliente)  
        #exibi as informações formatadas
        print(f"Cliente: {cliente["nome"]} | Cidade: {cliente["cidade"]} | Total gasto: R$ {total:.4f}")
        
#Funçaõ principal que controla o menu do sistema
def menu():
    while True:
        # Exibe as opções disponiveis para o usuário
        print("\n **** Menu de Cadastro de Clientes ****")
        print("1. Cadastrar Cliente")
        print("2. Registrar Compra")
        print("3. Listar Clientes")
        print("4. Sair")
        
        #Capitura a opção do user
        opcao = input("Escolha uma opção:")
        
        #Executa a opção correspondente a opção 
        if opcao == "1":
            cliente = cadastra_cliente()
            print(f"cliente {cliente["nome"]} cadastrado com sucesso!")
        elif opcao == "2":
            if not clientes:
                print("Nenhum cliente cadastrado. Por favor, cadastre um cliente primeiro.")
            else:
                #listar os clientes para escolha
                for i, cliente in enumerate(clientes):
                    print(f"{i + 1}. {cliente["nome"]}")
                try:
                    # Usuário escolho o cliente pelo indice
                    escolha = int(input("Escolha o numero do cliente: ")) -1
                    registrar_compra(clientes[escolha])
                except(IndexError, ValueError):
                    print("Opção inválida.")
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
#chama a função inicial do programa

menu()

    