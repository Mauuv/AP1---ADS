def cria_matriz():
    matriz = []
    lista_c = []
    for l in range(5):
        for c in range(5):
            n = [int(input("Digite um valor inteiro aleatório: "))]
            lista_c = lista_c + n
        matriz = matriz + [lista_c]
        lista_c= []
    return(matriz)
        
def soma_l(matriz):
    soma = []
    soma_int = 0
    for l in matriz:
        for c in l:
            soma_int = soma_int + c
        soma = soma + [soma_int]
        soma_int=0
    print (soma)
    
def soma_c(matriz):
    i = 0
    i2 = 0
    soma_int = 0
    soma = []
    while i<len(matriz):
        while i2<len(matriz):
            soma_int = soma_int + matriz[i2][i]
            i2 += 1
        soma = soma + [soma_int]
        soma_int = 0
        i2 = 0
        i += 1
    print(soma)    

def soma_dp(matriz):
    i=0
    produto = 1
    while i<len(matriz):
        produto = produto * matriz[i][i]
        i += 1
    print(produto)
        
matriz = cria_matriz()
soma_l(matriz)
soma_c(matriz)
soma_dp(matriz)