#Miniproyecto 6
#Bryann Alfaro
#Raul Jimenez
#Donaldo Garcia

#Ejercicio 1

#Referencia: https://relopezbriega.github.io/blog/2017/01/10/introduccion-a-los-metodos-de-monte-carlo-con-python/
#https://medium.com/@juee_thete/understanding-monte-carlo-simulation-and-its-implementation-with-python-3ecacb958cd4


import random
import matplotlib.pyplot as plt

acumulador = 0
probabilidades = []
for i in range(1000):

    #Se genera un aleatorio simulando la moneda y se agrega a lo anterior
    acumulador += random.randint(0,1)

    #Se calcula la probabilidad tomando en cuenta la iteracion y
    #el acumulado
    probabilidades.append(acumulador/(i+1))

    #Plot de la probabilidad
    plt.plot(probabilidades)


print(probabilidades[-1])
plt.show()




