class Carro:
    
    def __init__(self, gasto):
        self.gasto = gasto
        self.gasolina = 0

    def andar(self, kilometragem):
        if (self.gasto > kilometragem):
            gasto = kilometragem / self.gasto
            self.gasto -= gasto
            print("Seu Dodge Challenger andou exatamente {} kms, e para isso gastou um total de exatos {} litros de gasolina." .format(kilometragem, gasto))

        else:
            print("O challenger não possui gasolina no seu tanque. Para poder dirigir, abasteça por favor...")

    def totalGasolina(self):
        print("O atual nível de gasolina é {}." .format(self.gasolina))

    def adicionarGasolina(self, gasolina):
        self.gasolina += gasolina
        print("Você adicionou uma quantia de {}, agora seu total é de {} litros de gasolina." .format(self.gasolina, gasolina))