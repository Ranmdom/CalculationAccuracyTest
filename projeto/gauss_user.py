import numpy as np
def metodo_gauss(A, b): 
    n = len(A)

    #Fase de eliminação 
    for i in range(n): 
        # Pivotamento parcial
        max_index = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_index][i]):
                max_index = k
        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]

        #Eliminação de Gauss
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Fase de retrosubstituição
    x = [0] * n 
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x[i]
    
    return x

# Pedir ao usuário para inserir os coeficientes da Matriz A

#n = int(input("Digite o número de linhas / colunas da Matriz A: "))
#print("Agora digite os elementos da matriz A linha por linha: ")
#A = [] 
#for i in range(n): 
    #linha = list(map(float, input().split()))
    #A.append(linha)

# Pedir ao usuário para inserir os elementos do vetor b 

#print("Agora digite os elementos do vetor b: ")#
#b = list(map(float, input().split()))

# Resolver o sistema pelo método de gaus
#solucao = metodo_gauss(A, b)
#print("Solução do sistema: ", solucao)