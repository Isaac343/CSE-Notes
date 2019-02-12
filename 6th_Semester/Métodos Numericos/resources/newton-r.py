import numpy
iter = int(input('Número de iteraciones deseadas: '))
initial = input('Valor inicial de X: ')
xi = initial
for a in range(iter):
    xii = xi - ((2*xi*numpy.cos(2*xi) - (xi -2)^2)/(-4*xi*numpy.sin(2*xi) + 2*numpy.cos(2*xi)- 2(x-2)))
    temp_one = xii
    error = ((xii)-(xi)/xii)*100
    print(xii, ' ', error)
