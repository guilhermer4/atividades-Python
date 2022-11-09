from passagem import Excursao

excursao_0 = Excursao("Rock in Rio")
excursao_1 = Excursao("CCXP")
excursao_2 = Excursao("San Diego Comic-Con")
excursao_3 = Excursao("Dubai")
excursao_4 = Excursao("Londres")
excursao_5 = Excursao("Estados Unidos")
excursao_6 = Excursao("Espaço")

print("Bem vindo(a) !\nPossuímos ofertas de passagem para você conhecer alguns dos eventos e pontos turísticos que mais estão em alta, com um lugar bônus no pacote ! \n")
cliente = input("Insira seu nome para começar as compras: ")
print(cliente,", Possuímos 6 opções de excursão para você, escolha a opção desejada e divirta-se !\n [0] - Rock in Rio\n [1] - CCXP\n [2] - San Diego Comic-Con\n [3] - Dubai\n [4] - Londres\n [5] - Estados Unidos\n [6] - Espaço")

selecao = int(input("Escolha o número do pacote para começar: "))

lista_passagem = [excursao_0, excursao_1, excursao_2, excursao_3, excursao_4, excursao_5, excursao_6]

opcao_sel = int(selecao)

for opcao in lista_passagem:
    if opcao_sel >= 6:
        print("\nNão foi possível completar a operação, tente novamente...")
        break
    if opcao_sel <= 5:
        print(cliente,"seu pacote escolhido foi ", lista_passagem[opcao_sel].pacote)
        print("Operação realizada com sucesso, divirta-se e volte sempre !")
        break