#para entregar 01 lista 
#autor: Maurício Tonin Verona
def main():
    import os

    clear = lambda: os.system('cls')
    clients = []
    opcao = 1

    while opcao != 0:
        menu()
        opcao = int(input('Digite a opcção que você deseja: '))
        while opcao < 0 and opcao > 5:
            print('ERRO')
        if opcao == 1:
            clear()
            clients = cadastro_cliente(clients)
        if opcao == 2:
            clear()
            print(busca_cliente(clients))
        if opcao == 3:
            clear()
            clients = exclui_cliente(clients)
        if opcao == 4:
            clear()
            percorre_lista(clients)

    clear()
    print("Encerrando...")

def menu():
    print('''Escolha a opção que deseja
1 - Adicionar clientes
2 - Buscar cliente por nome
3 - Excluir cliente
4 - Listar clientes
0 - Finalizar programa''')

def cadastro_cliente(clients):
    nome = input('Digite o nome do cliente a ser cadastrado: ')
    email = input('Digite o email do cliente a ser cadastrado: ')
    clients = clients + [[nome, email]]
    return(clients)

def busca_cliente(clients):
    buscador = input('Digite o nome a ser buscado: ')
    lista_aux = []
    i=0
    for l in clients:
        for c in l:
            if buscador.lower() == c.lower():
                lista_aux = lista_aux + [clients[i]]
        i = i + 1
    return(lista_aux)

def exclui_cliente(clients):
    buscador = input('Digite o nome a ser excluido: ')
    i = 0
    for l in clients:
        for c in l:
            if buscador.lower() == c.lower():
                del(clients[i])
        i = i + 1
    return(clients)

def percorre_lista(clients):
    for l in clients:
        for c in l:
            print(c, end=" ")
        print()

main()