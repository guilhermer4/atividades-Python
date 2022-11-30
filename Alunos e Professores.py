class Alunos:
    def __init__(self, nome, sobrenome, documento, curso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.documento = documento
        self.curso = curso

class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo
    
class Professor:
    def __init__(self, nome, disciplina, siape, curso):
        self.nome = nome
        self.disciplina = disciplina
        self.siape = siape
        self.curso = curso