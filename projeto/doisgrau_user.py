import numpy as np

# Métodos quadraticos 

# Fórmula: f(x) = ax² + bx + C
def ajuste_curva(x,y):
    n = len(x)  #Número de dados 
    sum_x = sum(x) # Soma de todos os valores de x
    sum_x2 = sum(x**2) # Soma de todos os valores ao quadrado 
    sum_x3 = sum(x**3) # Soma de todos os valores ao cubo
    sum_x4 = sum(x**4) # Soma das quartas potências de todos os valores em x 
    sum_y = sum(y) #Soma de todos os valores em y
    sum_xy = sum(x*y) #Soma de todos os produtos de cada elemento em x e y 
    sum_x2y = sum(x**2 * y) #A soma dos produtos de cada elemetente em x² e y

    #Resovlendo o sistema de equações normais

    #Matrizes de coeficientes das equações normais  
    A = np.array([[n, sum_x, sum_x2],
                  [sum_x, sum_x2, sum_x3],
                  [sum_x2, sum_x3, sum_x4]])
    
    # Vetor de termos independentes das equações normais 
    b = np.array([sum_y, sum_xy, sum_x2y])

    #Encontrando os coeficientes a, b e c 
    a, b, c = np.linalg.solve(A, b)

    return a, b, c

# Pedir ao usuário para inserir os dados de entrada 
#n = int(input("Digite o número de pontos de dados: "))
#print("Agora digite os valores de x e y para cada ponto de dados (separados por espaço): ")
#x = [] 
#y = [] 

#for _ in range(n):
    ponto = input().split()
    x.append(float(ponto[0]))
    y.append(float(ponto[1]))

#x = np.array(x)
#y = np.array(y)

#Ajuste de curva quadrática

#a, b, c = ajuste_curva(x, y)
#print("\nCoeficientes da curva quadrática: a =",a ,", b =",b ,", c =", c)