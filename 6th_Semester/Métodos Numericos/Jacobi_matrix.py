from numpy import *
m1 = []
m_y = int(input('Altura de la matriz: '))
m_x = int(input('Largo de la matriz: '))
for a in range(m_y):
    m1.append([])
    for b in range(m_x):
        data = float(input('valor: '))
        m1[a].append(data)

print (m1)
