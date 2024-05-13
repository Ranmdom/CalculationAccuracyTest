import numpy as np

def f(x):
    return np.exp(x**2) - x


#Método da bisseção para o zero da função 
def metodo_bissecao(f, a ,b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("Não é possível garantir a existência de uma raiz no intervalo fornecido.")
        return None
    else: 
        for i in range(max_iter):
            c = (a + b) / 2
            if np.abs(f(c)) < tol:
                return c
            elif f(c) * f(a) < 0:
                b = c 
            else: 
                a = c
            
        print("O método da bisseção atingiu o número máximo de iterações")
        return None
        
#Método de newton-raphson parando em 4 iterações 
def metodo_newton_rapshon(f, df, x0, tol=1e-6, max_iter=100):
    for i in range(4):
        x1 = x0 - f(x0) / df(x0)
        if np.abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("O método da de Newton-Raphson atingiu 4 iterações")
    
    #Retorna a aproximação obtida após 4 iterações 
    return x1

def df(x): 
    return 2 * x * np.exp(x**2) - 1

#Intervalo inicial para o método da bissção 
#a = float(input("Digite o limtie inferior do intervalo inicial: "))
#b = float(input("Digite o limite superior do intervalo inicial: "))

#Chamar o método d bisseção 
#root_bissecao = metodo_bissecao(f,a,b)
##if root_bissecao is not None:
    #print("Raiz encontrada pel##o método da bisseção: ", root_bissecao)

#Chute inicial para o método de Newthon-Raphson 
#x0 = float(input("DIgite o chute para o método de Newthon-Raphson"))

#Chamar o método de Newthon-Rapshon
#root_newton_raphson = metodo_newton_rapshon(f, df, x0)
#if root_newton_raphson is not None:
    #print("Raiz encontrada pelo método de Newton-Raphson: ", root_newton_raphson)