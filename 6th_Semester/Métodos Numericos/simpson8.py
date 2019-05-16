import math

inter = 4
inf = float(input("limite inferior: "))
sup = float(input("limite superior: "))

intervalos_array, functions_array = [], []
caudal = []
concentracion = []

h  = (sup - inf) / inter
round(h, 6)
b = 0

intervalos_array.append(inf)
medium_1 = ((2*inf)+sup)/3
intervalos_array.append(medium_1)
medium_2 =(inf + (2*sup)) / 3
intervalos_array.append(medium_2)
intervalos_array.append(sup)

for c in range (0, inter):
    cs2 = ((1 + math.cos(2*0.4 * intervalos_array[c])) / (2))
    round(cs2, 6)
    Q_value = (9 + (4 * cs2))
    c_value = (5 * math.e**(-0.5*intervalos_array[c])) + (2*math.e**(0.15*intervalos_array[c]))
    print(c_value)
    main_value = Q_value * c_value
    caudal.append(Q_value)
    concentracion.append(c_value)
    functions_array.append(main_value)


print(functions_array)
result = ((3*h)/8)*(functions_array[0] + (3*functions_array[1]) + (3*functions_array[2]) + functions_array[3])
for h in range(inter):
    print("%i | %.6f | %.6f" % (h, intervalos_array[h], functions_array[h]))
print("%.6f" % (result))
