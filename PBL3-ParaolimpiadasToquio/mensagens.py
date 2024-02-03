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

def tela_apresentacao():
    apresentacao = '''
+----------------------------------------------------------------------------------+
|             Bem-vindo(a) ao sistema UEFS pelos Atletas Paralímpicos              |
|Um programa criado por alunos da UEFS em parceria com o Comitê Olímpico Brasileiro|
+----------------------------------------------------------------------------------+'''
    return apresentacao

def tela_menu():
    menu = '''
+------------------------------+
|             MENU             |
+------------------------------+
| 1 - Cadastrar um novo atleta |
|     2 - Editar Cadastro      |
|     3 - Excluir Cadasto      |
|   4 - Visualizar Cadastros   |
| 5 - Relátorio de Informações |
|      6 - Salvar e Sair       |
+------------------------------+\n'''
    return menu

def tela_menu_relatorio():
    menu_relatorio = '''
+-----------------------------------+
|             RELATÓRIO             |
+-----------------------------------+
| 1 - A quantidade de atletas que   |
|  participaram dos jogos separados | 
|        por modalidade e sexo      |
|      2 - Relação dos atletas      |
|    diagnosticados com Covid-19    |
|  separados por modalidade e sexo  |
|       3 - Quadro de medalhas      |
|       4 - Dados dos atletas       |
|      que conquistaram medalhas    |
|   5 - Relatório de Modalidades    |
|             (Brasil)              |
|     6 - Todas opções acima        |
|       7 - Sair para o Menu        |
+-----------------------------------+\n'''
    return menu_relatorio

def tela_menu_edicao():
    menu_edicao='''
+------------------------------+
|             EDITAR           |
+------------------------------+
|           1 - Nome           |
|          2 - Idade           |
|           3 - Sexo           |
|        4 - Paralisia         |
| 5 - Diagnóstico de COVID-19  |
|        6 - Modalidade        |
|         7 - Medalhas         |
|    8 - Sair para o Menu      |
+------------------------------+\n'''
    return menu_edicao

def tela_cabecalho_cadastro():
    cabecalho_cadastro = '''
+------------------------------+
|           CADASTRO           |
+------------------------------+'''
    return cabecalho_cadastro

def tela_cabecalho_edicao():
    cabecalho_edicao = '''
+------------------------------+
|            EDIÇÃO            |
+------------------------------+'''
    return cabecalho_edicao

def tela_cabecalho_excluir():
    cabecalho_excluir = '''
+------------------------------+
|           EXCLUSÃO           |
+------------------------------+'''
    return cabecalho_excluir

def tela_cabecalho_dados():
    cabecalho_dados = '''
+------------------------------+
|            DADOS             |
+------------------------------+'''
    return cabecalho_dados