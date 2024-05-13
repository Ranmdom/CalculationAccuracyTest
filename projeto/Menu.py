import numpy as np

from gauss_user import metodo_gauss
from bissecao_user import f, metodo_bissecao, metodo_newton_rapshon, df
from doisgrau_user import ajuste_curva
from Gauss_jacobi import gauss_jacobi

def menu(): 
    while True:
        print("\nEscolha uma opção: ")
        print("[1] - ZeroFunção : Bisseção")
        print("[2] - ZeroFunção: Newton-Raphson")
        print("[3] - Ajuste De Curva: Função 2 grau ")
        print("[4] - Sistema Equação Linerares: Gauss")
        print("[5] - Sistema Equação Lineares: Gauss-Jacob")
        print("[0] - Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == '1':
            #Intervalo inicial para o método da bissção 
            a = float(input("Digite o limite inferior do intervalo inicial: "))
            b = float(input("Digite o limite superior do intervalo inicial: "))
            root_bissecao = metodo_bissecao(f, a, b)
            if root_bissecao is not None:
                print("Raiz encontrada pelo método da bisseção: ", root_bissecao)

        elif escolha == '2': 
            x0 = float(input("Digite o chute para o método de Newton-Raphson: "))
            root_newton_raphson = metodo_newton_rapshon(f, df, x0)
            if root_newton_raphson is not None:
                print("Raiz encontrada pelo método de Newton-Raphson: ", root_newton_raphson)

        elif escolha == '3': 
            # Pedir ao usuário para inserir os dados de entrada 
            n = int(input("Digite o número de pontos de dados: "))
            print("Agora digite os valores de x e y para cada ponto de dados (separados por espaço): ")
            x = [] 
            y = [] 

            for _ in range(n):
                ponto = input().split()
                x.append(float(ponto[0]))
                y.append(float(ponto[1]))

            x = np.array(x)
            y = np.array(y)

            a, b, c = ajuste_curva(x, y)
            print("Coeficiente da curva quadrática: a= ", a, ", b =", b, ", c =", c)
        
        elif escolha == '4':
            # Pedir ao usuário para inserir os coeficientes da Matriz A

            n = int(input("Digite o número de linhas / colunas da Matriz A: "))
            print("Agora digite os elementos da matriz A linha por linha: ")
            A = [] 
            for i in range(n): 
                linha = list(map(float, input().split()))
                A.append(linha)

            # Pedir ao usuário para inserir os elementos do vetor b 

            print("Agora digite os elementos do vetor b: ")
            b = list(map(float, input().split()))           
            solucao = metodo_gauss(A, b)
            print("Solução do sistema: ", solucao)
        
        elif escolha == '5': 
            # Pedir ao usuário para inserir a matriz A
            n = int(input("Digite o número de linhas/colunas da matriz A: "))
            print("Agora digite os elementos da matriz A linha por linha:")
            A = []
            for i in range(n):
                linha = list(map(float, input().split()))
                A.append(linha)

            A = np.array(A)
            
            # Pedir ao usuário para inserir o vetor b
            print("Agora digite os elementos do vetor b:")
            b = np.array(list(map(float, input().split())))

            # Pedir ao usuário para inserir o chute inicial x0
            print("Agora digite os elementos do chute inicial x0:")
            x0 = np.array(list(map(float, input().split())))
            solucao = gauss_jacobi(A, b, x0)
            if isinstance(solucao, np.ndarray):  # verificar se é uma matriz ou não 
                print("Solução do sistema: ", solucao)
            else: 
                print(solucao)
        
        elif escolha == '0': 
            print('Saindo...')
            break
        else:
            print("Opção inválida! Tente apenas números")
        
menu() 
