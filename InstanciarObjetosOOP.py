class CalcCubo:
    '''Classe que permite calcular a área de um Cubo'''
    def __init__(self, valor):
        self.x = valor
        print('Objeto criado')
    def calcular_cubo(self):
        self.cubo = self.x * self.x * 6 
        return 'Cubo calculado:' + str(self.cubo)

num = int(input('Insira o lado do seu quadrado:   '))
objCub1 = CalcCubo(num)
cubo = objCub1.calcular_cubo()
num = int(input('Insira o lado do seu quadrado:   '))
objCub2 = CalcCubo(num)
cubo2 = objCub2.calcular_cubo()
print(cubo)
print(cubo2)