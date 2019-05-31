import matplotlib.pyplot as plt
# t = 0.23
# a = 0.125
# b = 0.250
# c = 0.375
# A = 6.24
# B = 7.74
# C = 4.85
# x_1 = ((t-b)/(a-b)) * ((t-c)/(a-c)) * (A)
# x_2 = ((t-a)/(b-a)) * ((t-c)/(b-c)) * (B)
# x_3 = ((t-a)/(c-a)) * ((t-b)/(c-b)) * (C)
# result = x_1 + x_2 + x_3
# round(6, result)
# print(result)

esf = [5, 10, 15, 20, 25, 30, 35, 40]
t= [40, 30, 25, 40, 18, 20, 22, 15]

e = 13
x0 = ((e-esf[1])/(esf[0]-esf[1]))*((e-esf[2])/(esf[0]-esf[2]))*((e-esf[3])/(esf[0]-esf[3]))*(t[0])
x1 = ((e-esf[0])/(esf[1]-esf[0]))*((e-esf[2])/(esf[1]-esf[2]))*((e-esf[3])/(esf[1]-esf[3]))*(t[1])
x2 = ((e-esf[0])/(esf[2]-esf[0]))*((e-esf[1])/(esf[2]-esf[1]))*((e-esf[3])/(esf[2]-esf[3]))*(t[2])
x3 = ((e-esf[0])/(esf[3]-esf[0]))*((e-esf[1])/(esf[3]-esf[1]))*((e-esf[2])/(esf[3]-esf[2]))*(t[3])


esf = [720, 740, 760, 780]
t= [0.12184, 0.1406, 0.15509, 0.16643]
e = 750
x0 = ((e-esf[1])/(esf[0]-esf[1]))*((e-esf[2])/(esf[0]-esf[2]))*((e-esf[3])/(esf[0]-esf[3]))*(t[0])
x1 = ((e-esf[0])/(esf[1]-esf[0]))*((e-esf[2])/(esf[1]-esf[2]))*((e-esf[3])/(esf[1]-esf[3]))*(t[1])
x2 = ((e-esf[0])/(esf[2]-esf[0]))*((e-esf[1])/(esf[2]-esf[1]))*((e-esf[3])/(esf[2]-esf[3]))*(t[2])
x3 = ((e-esf[0])/(esf[3]-esf[0]))*((e-esf[1])/(esf[3]-esf[1]))*((e-esf[2])/(esf[3]-esf[2]))*(t[3])


result = x0 + x1 + x2 + x3
print('para ', e,' = ', result)
