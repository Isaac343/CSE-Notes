class Jacobi():

    def __init__(self):
        self.ci_1 = 0
        self.ci_2 = 0
        self.ci_3 = 0

    def evaluation(self, tst):
        print('C1 ', ' C2 ', ' C3 ', ' Ea ')
        print(self.ci_1, ' ', self.ci_2, ' ', self.ci_3, '  -' )
        for a in range(tst):
            self.back = self.ci_1
            self.c_1 = ((3300 + self.ci_2 + self.ci_3)/(15))
            self.c_2 = ((1200 + 3*self.ci_1 + 6*self.ci_3)/(18))
            self.c_3 = ((2400 + 4*self.ci_1 + self.ci_2)/(12))
            self.bac_v = ((self.c_1 - self.back)/(self.c_1))*100
            print(self.c_1, ' ', self.c_2, ' ', self.c_3, self.bac_v)
            self.ci_1 = self.c_1
            self.ci_2 = self.c_2
            self.ci_3 = self.c_3




tst = int(input('número de iteraciones: '))
Aa = Jacobi()
Aa.evaluation(tst)
