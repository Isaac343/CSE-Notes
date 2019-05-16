import math

inter = int(input("número de intervalos: "))
inf = float(input("limite inferior: "))
sup = float(input("limite superior: "))

intervalos_array, functions_array = [], []
caudal = []
concentracion = []

h  = (sup - inf) / inter
round(h, 6)
b = 0

intervalos_array.append(inf)
for a in range(0, inter-1):
    b = b + h
    data = inf + b
    intervalos_array.append(data)
intervalos_array.append(sup)

print(intervalos_array)
for c in range(0, inter+1):
    cs2 = ((1 + math.cos(2*0.4 * intervalos_array[c])) / (2))
    round(cs2, 6)
    Q_value = (9 + (4 * cs2))
    c_value = (5 * math.e**(-0.5*intervalos_array[c])) + (2*math.e**(0.15*intervalos_array[c]))
    print(c_value)
    main_value = Q_value * c_value
    caudal.append(Q_value)
    concentracion.append(c_value)
    functions_array.append(main_value)

medium = 0
for d in range (1, inter):
    medium = medium +  functions_array[d]

resultado = (sup-inf)*((functions_array[0] + (2*(medium)) + functions_array[inter]) / (2*inter))

for z in range(inter+1):
    print("%i | %.6f | %.6f | %.6f" % (intervalos_array[z], caudal[z], concentracion[z], functions_array[z]))
print("%.6f" % (resultado))
