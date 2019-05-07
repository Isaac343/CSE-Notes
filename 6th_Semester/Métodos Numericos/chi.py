import math

v = int(input('Valor de "v": '))# grados de libertad (n-1)
x, odds, pairs = 0, 0, 0

intervalos =int(input('Número de intervalos para Simpson 1/3: '))
sup_lim = float(input('Límite superior: '))
inf_lim = float(input('Limite inferior: '))

intervalos_array, functions_array = [], []

h = (sup_lim - inf_lim) / intervalos
round(h, 6)
print(h)
b = 0
intervalos_array.append(inf_lim)
for a in range(0, intervalos-1):
    b = b + h
    data = inf_lim + b
    intervalos_array.append(data)
intervalos_array.append(sup_lim)

for c in range(0, intervalos+1):
    fun_value = ((1) / (2**(v/2) * math.gamma(v/2))) * (intervalos_array[c]**((v/2)-1)) * (math.e**(-intervalos_array[c]/2))
    functions_array.append(fun_value)

for d in range(1, intervalos):
    if d%2 != 0:
        odds = odds + functions_array[d]
    elif d%2 == 0:
        pairs =pairs + functions_array[d]

result = (sup_lim - inf_lim)*((functions_array[0] + (4*odds) + (2*pairs) + functions_array[intervalos])/ (3*intervalos))

for h in range(intervalos+1):
    print("%i | %.6f | %.6f" % (h, intervalos_array[h], functions_array[h]))
print("%.6f" % (result))
