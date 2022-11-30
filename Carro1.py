from carro import Carro:

challenger = Carro(70)

print("Você tem um Dodge Challenger e a sua kilometragem é de exatos 70 km e seu tanque está vazio. Por favor, abasteça para poder dirigir...")

challenger.addicionarGasolina(20)

challenger.andar(10)

challenger.totalGasolina()

print(vars(challenger))