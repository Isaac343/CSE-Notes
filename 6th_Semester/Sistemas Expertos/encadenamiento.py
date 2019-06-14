# Decision de inversiòn se encuentra las siguientes variables involucradas variable
# A que tiene 10,000
# B es menor de 30
# C Tiene educacion de nivel universitario
# D tiene inreso anual de almenos 40,000
# E Debe invertir en valores
# F Debe invertir en acciones de crecimiento
# G invertir en acciones de IBM
# Cada una de estas variables puede ser verdadera o falsa los echos son los siguientes supongamos que un inversor tiene 10,000 y tiene 25 años y este le gustaria recibir consejos sobre la inversiòn IBM  entonces esto sabe que
# A es verdadero y B es verdadero
#
# 1. Supongamos que nuestra base de conocimiento, si una persona tiene 10,000 y tiene u titulo universitario entonces debería invertir en valores,
# 2. SI el ingreso anual de una persona es de almenos 40,000 y tiene un titulo universitario entonces deberia invertir en acciones de crecimiento
# 3. SI una persona es menor de 30 años y esta invirtiendo en valores entonces debería de invertir en acciones de crecimiento
# 4. SI una persona es menor de 30 años entonces tiene un titulo universitario
# 5. SI una persona quiere invertir en acciones de crecimiento entonces deberia inbertir en acciones de IBM
#
# Entonces estas reglas se pueden escribir de esta manera
#
# 1. Si A entonces C luego E
# 2. Si D y C luego F
# 3. Si B y E entonces F
# 4. Si B entonces C
# 5. Si F entonces G
# G, F,  (B,E(A,C))
B = int(input('edad: '))
A = int(input('saldo acutual: '))
D = int(input('ingresos anuales: '))
E = 'Debe invertir en valores'
F = 'Debe invertir en acciones de crecimiento'
G = 'Debe invertir en IBM'


if A >= 10000:
    C = True
    print('usted tiene un titulo universitario')
    Ee = True
    print(E)
elif A < 10000:
    C = False
    Ee = False

if B <= 30:
    C = True
elif B > 30:
    C = False

if B <= 30:
    if Ee == True:
        print(F)
        Ff = True
    if Ee == False:
        Ff = False

if D >= 40000:
    if C == True:
        print(F)
        Ff = True

if Ff == True:
    print(G)
