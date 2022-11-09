class Cadastro:
    def __init__(self, nome, sobrenome, idade, genero, endereco, mensagem):
        print("Iniciando um cadastro")
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.genero = genero
        self.endereco = endereco
        self.mensagem = mensagem

    def certifique_seu_nome(self, resposta):
        print(self.nome)
        if resposta == "y":
            print("Nome correto")
        else:
            print("Nome inválido")

    def certifique_seu_sobrenome(self, resposta):
        print(self.sobrenome)
        if resposta == "y":
            print("Sobrenome correto")
        else:
            print("Sobrenome inválido")

    def certifique_sua_idade(self, resposta):
        print(self.idade)
        if resposta == "18":
            print("Idade válida")
        else:
            print("Negado, restrição de idade")

    def certifique_seu_genero(self, resposta):
        print(self.genero)
        if resposta == "1":
            print("Masculino")
        if resposta == "2":
            print("Feminino")

    def certifique_seu_endereco(self, resposta):
        print(self.endereco)
        if resposta == "y":
            print("Endereço válido")
        else:
            print("Endereço inválido")

    def mensagem_para(self, destino, msg):
        destino.mensagem += msg

    def mostrar_dados(self):
        print('nome', self.nome, 'sobrenome', self.sobrenome, 'idade', self.idade, 'genero', self.genero, 'endereco', self.endereco)

class adicionais:
    print("Nome: Guilherme")
    print("Sobrenome: Ribeiro")
    print("Idade: 18 anos")
    print("Gênero: Masculino")
    print("Endereço: Rua Reinaldo Sbardeloto, 576")
    print("Ano de Nascimento: 30 de Abril de 2004")
    print("Cidade: Sertão")