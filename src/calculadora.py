class Calculadora:

    def __init__(self, adicao, subtracao):
        self.adicao = adicao
        self.subtracao = subtracao
    
    def add(self, number1, number2, op):
        if op:
            return self.adicao.soma(number1, number2)
        return None
    
    def sub(self, number1, number2, op):
        if op:
            return self.subtracao.diferenca(number1, number2)
        return None
