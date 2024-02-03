'''/*******************************************************************************
Autor: João Victor Alves Cerqueira
Componente Curricular: MI - Algoritmos (TP04)
Concluido em: 05/12/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''

from modalidades import *

class Atleta():
    def __init__(self, nome, sexo, idade, modalidade, medalhas, paralisia, covid):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.paralisia = paralisia
        self.covid = covid
        self.modalidade = modalidade
        self.medalhas = medalhas
    
    def __repr__(self):
        sexo = "Feminino" if self.sexo == "f" else "Masculino"
        covid = "Positivo" if self.covid else "Negativo"
        modalidade = (self.modalidade.name).title().replace("_", " ")
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {sexo}\nTipo de paralisia: {self.paralisia}\nDiagnostico COVID-19: {covid}\nModalidade: {modalidade}\nMedalhas:\nOuro - {self.medalhas[0]}\nPrata - {self.medalhas[1]}\nBronze - {self.medalhas[2]}"
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        assert value.replace(" ", '').isalpha(), "Nome com caractéres inválidos!"
        self._nome = value
    
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, value):
        assert value == "m" or value == "f", "Sexo inválido!"
        self._sexo = value

    @property
    def paralisia(self):
        return self._paralisia

    @paralisia.setter
    def paralisia(self,value):
        assert value.replace(" ", '').isalpha(), "Paralisia com caractéres inválidos"
        self._paralisia = value
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        assert value.isdigit(), "Idade com caractéres inválidos!"
        assert int(value) >= 0 and int(value) <= 100, "A idade deve ser maior que 0 e menor que 100!"
        self._idade = int(value)
    
    @property
    def covid(self):
        return self._covid
    
    @covid.setter
    def covid(self, value):
        assert value == "s" or value == "n", "Diagnóstico de COVID inválido!"
        self._covid = True if value == "s" else False

    @property
    def modalidade(self):
        return self._modalidade
    
    @modalidade.setter
    def modalidade(self,value):
        assert value.isdigit(), "Modalidade com caractéres inválidos!"
        assert int(value) >= 0 and int(value) <= 21, "Modalidade Inválida!"
        self._modalidade = Modalidades(int(value))
    
    @property
    def medalhas(self):
        return self._medalhas

    @medalhas.setter
    def medalhas(self,value):
        assert len(value) == 3, "Lista de medalhas com tamamho incorreto"
        assert type(value) is list, "Medalhas com tipo Inválido"
        for i in range(len(value)):
            assert value[i].isdigit(), "Medalhas com caractéres inválidos!"
            value[i] = int(value[i])
        self._medalhas = value