class gauss_seidel():

    def __init__(self):
        self.a, self.b, self.c, self.d, self.e = 0, 0, 0, 0, 0

    def value(self, iterations):
        print("N°| ~~~X1~~~ | ~~~X2~~~ | ~~~X3~~~ | ~~~X4~~~ | ~~~X5~~~ | ~~~Ea~~ |")
        for nu in range(iterations):
            self.back = self.a

            self.a = (5 + (2*self.b) + self.c) / (8)
            self.b = (2 + (2*self.a) + (4*self.c) + self.d) / (9)
            self.c = (1 + self.a + (3*self.b)+ self.d + (2*self.e)) / (7)
            self.d = (1 + (4*self.b) + (2*self.c) + (5*self.e)) / (12)
            self.e = (5 + (7*self.c) + (3*self.d)) / (15)
            self.error = ((self.a - self.back)/self.a) * 100
            print("%i | %.6f | %.6f | %.6f | %.6f | %.6f | %.2f" % (nu+1, self.a, self.b, self.c, self.d, self.e, self.error))



iterations = int(input('Número de iteraciones: '))
Aa = gauss_seidel()
Aa.value(iterations)
