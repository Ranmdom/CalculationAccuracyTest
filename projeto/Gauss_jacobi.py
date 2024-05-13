import numpy as np

def gauss_jacobi(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    x_prev = x0.copy()
    
    for _ in range(max_iter):
        for i in range(n):
            sum_val = 0
            for j in range(n):
                if j != i:
                    sum_val += A[i][j] * x_prev[j]
            x[i] = (b[i] - sum_val) / A[i][i]

        if np.linalg.norm(x - x_prev) < tol:
            return x, "Convergência alcançada após {} iterações.".format(_ + 1)
        
        x_prev = x.copy()
    
    return x, "Falha: Convergência não alcançada após o número máximo de iterações."

# Pedir ao usuário para inserir a matriz A
#n = int(input("Digite o número de linhas/colunas da matriz A: "))
#print("Agora digite os elementos da matriz A linha por linha:")
#A = []
#for i in range(n):
    #linha = list(map(float, input().split()))
    #A.append(linha)

#A = np.array(A)

# Pedir ao usuário para inserir o vetor b
#print("Agora digite os elementos do vetor b:")
#b = np.array(list(map(float, input().split())))

# Pedir ao usuário para inserir o chute inicial x0
#print("Agora digite os elementos do chute inicial x0:")
#x0 = np.array(list(map(float, input().split())))

# Resolver o sistema pelo método de Gauss-Jacobi
#solucao, mensagem = gauss_jacobi(A, b, x0)
#print("\nSolução do sistema:", solucao)
#print("Mensagem:", mensagem)
