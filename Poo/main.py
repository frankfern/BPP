class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        result = self.num1 + self.num2
        print(f'La resultado de {self.num1} + {self.num2} = {result}')

    def multiplicar(self):
        result = self.num1 * self.num2
        print(f'La resultado de {self.num1} * {self.num2} = {result}')

    def restar(self):
        result = self.num1 - self.num2
        print(f'La resultado de {self.num1} - {self.num2} = {result}')

    def dividir(self):
        result = self.num1 / self.num2
        print(f'La resultado de {self.num1} / {self.num2} = {result}')


if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    calculadora.sumar()
    calculadora.multiplicar()
    calculadora.restar()
    calculadora.dividir()
