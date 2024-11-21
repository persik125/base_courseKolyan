import matplotlib.pyplot as plt
def parabola(x0,xk,n,a,b,c):
    x = [i for i in range(x0,xk,(xk-x0)/n)]
    y = [a*j**2 + b*j + c for j in x]
    plt.plot(x,y) 
    plt.savefig('myparabola.png') # сохранение графика