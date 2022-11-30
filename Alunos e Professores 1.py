from classes import Alunos

ads = Curso("Análise e desenvolvimento de Sistenas", "Matinal")
agronomia = Curso("Agronomia", "Integral")
biologia = Curso("Licenciatura em Ciências Biológicas", "Matinal")

aluno_guilherme = Alunos("Guilherme", "Ribeiro", "01", ads)
aluno_ana = Alunos("Ana Júlia", "Della Vecchia", "02", agronomia)
aluno_eliedson = Alunos("Eliedson", "de Souza", "03", biologia)

profluis = Professor("Luis", "Redes", "01", ads)
profcheila = Professor("Cheila", "Engenharia de Software", "02", agronomia)
profmh = Professor("Maria Helena", "Lógica de Programação", "02", biologia)

print(aluno_guilherme.curso.nome)
print(aluno_ana.curso.nome)
print(aluno_eliedson.curso.nome)

print(profluis.disciplina.nome)
print(profcheila.disciplina.nome)
print(profmh.disciplina.nome)