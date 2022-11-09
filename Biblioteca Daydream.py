from biblioteca import Biblioteca

quadrinho_0 = Biblioteca("A Saga da Fênix Negra")
quadrinho_1 = Biblioteca("Demolidor: Born Again")
quadrinho_2 = Biblioteca("Batman – Ano Um")
quadrinho_3 = Biblioteca("Batman – O Cavaleiro das Trevas")
quadrinho_4 = Biblioteca("All Star Superman")
quadrinho_5 = Biblioteca("Crise nas Infinitas Terras")
quadrinho_6 = Biblioteca("A Saga das Trevas Eternas")
quadrinho_7 = Biblioteca("A Era do Apocalipse")
quadrinho_8 = Biblioteca("Homem-Aranha – A Última Caçada de Kraven")
quadrinho_9 = Biblioteca("V de Vingança")
quadrinho_10 = Biblioteca("Guerra Civil")

print("Seja bem vindo(a) a biblioteca Daydream !\n onde você pode fugir da realidade e se embarcar no mundo da fantasia e vivenciar muitas aventuras com os nossos quadrinhos !\n")
cliente = input("Para começarmos, insira seu nome: ")
print(cliente,", Aqui está a nossa lista de quadrinhos, aproveite !\n [0] - A Saga da Fênix Negra\n [1] - Demolidor: Born Again\n [2] - Batman: Ano Um\n [3] - All Star Superman\n [4] - Crise nas Infinitas Terras\n [5] - A Saga das Trevas Eternas\n [6] - A Era do Apocalipse\n [7] - Homem-Aranha – A Última Caçada de Kraven\n [8] - V de Vingança\n [9] - Guerra Civil")

selecao = int(input("Escolha o quadrinho que você deseja: "))

lista_quadrinhos = [quadrinho_0, quadrinho_1, quadrinho_2, quadrinho_3, quadrinho_4, quadrinho_5, quadrinho_6, quadrinho_7, quadrinho_8, quadrinho_9, quadrinho_10]

opcao_sel = int(selecao)

for opcao in lista_quadrinhos:
    if opcao_sel >= 10:
        print("Este exemplar não foi encontrado, por favor, tente novamente...")
        break
    if opcao_sel <= 9:
        print("cliente,", seu quadrinho ", lista_quadrinhos[opcao_sel].quadrinho, "foi agendado com sucesso, esperamos a sua entrega do quadrinho.")
        print("Obrigado, volte sempre !")
        break