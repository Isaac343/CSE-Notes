import math

inter = int(input("número de intervalos: "))
inf = float(input("limite inferior: "))
sup = float(input("limite superior: "))

intervalos_array, functions_array = [], []
caudal = []
concentracion = []

h  = (sup - inf) / inter
round(h, 6)
b, odds, pairs = 0, 0, 0

intervalos_array.append(inf)
for a in range(0, inter-1):
    b = b + h
    data = inf + b
    intervalos_array.append(data)
intervalos_array.append(sup)

for c in range (0, inter+1):
    cs2 = ((1 + math.cos(2*0.4 * intervalos_array[c])) / (2))
    round(cs2, 6)
    Q_value = (9 + (4 * cs2))
    c_value = (5 * math.e**(-0.5*intervalos_array[c])) + (2*math.e**(0.15*intervalos_array[c]))
    print(c_value)
    main_value = Q_value * c_value
    caudal.append(Q_value)
    concentracion.append(c_value)
    functions_array.append(main_value)

for d in range(1, inter):
    if d%2 != 0:
        odds = odds + functions_array[d]
    elif d%2 == 0:
        pairs =pairs + functions_array[d]

result = (sup - inf)*((functions_array[0] + (4*odds) + (2*pairs) + functions_array[inter])/(3*inter))
for h in range(inter+1):
    print("%i | %.6f | %.6f" % (h, intervalos_array[h], functions_array[h]))
print("%.6f" % (result))
