import numpy as np

def f(x):
    return np.exp(x**2) - x


#Método da bisseção para o zero da função 

def f(x):
    try:
        return np.exp(x**2) - x
    except OverflowError:
        return np.inf  # Retornar um valor grande para indicar overflow
    

def bissecao(a, b, tol, max_iter):
    n = 0
    while n < max_iter:
        x = (a + b) / 2
        if abs(b - a) / 2 < tol or f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        n += 1
    return None  # Não convergiu dentro do limite de iterações

a = -2
b = 2
tolerancia = 1e-6
max_iteracoes = 100
        
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