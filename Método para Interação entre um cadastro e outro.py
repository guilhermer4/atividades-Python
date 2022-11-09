from classe import Cadastro

guilherme = Cadastro('Guilherme', 'Ribeiro', 18, 'Masculino', 'Rua Reinaldo Sbardeloto','')
eliedson = Cadastro('Eliedson', 'de Souza', 19, 'Masculino', 'Rua Angelo Menegueiro', '')

print(vars(guilherme))
print(vars(eliedson))

guilherme.certifique_seu_nome(input("Y para nome certo e N para nome errado"))

guilherme.mensagem_para(eliedson, input("Escreva a mensagem para" + eliedson.nome))


print(vars(eliedson))