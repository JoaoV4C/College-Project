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
import jsonpickle
import os
from atletas import Atleta
from mensagens import *

# Função de deletar um atleta da lista
def deletar_atleta(nome_atleta, atletas):
    confirmacao = validar_sim_nao(input(f"Tem certeza que deseja excluir o atleta {nome_atleta}? [S] ou [N]\n").lower())
    if confirmacao == "s":
        del atletas[nome_atleta]
        print(f"Atleta {nome_atleta} excluído com sucesso!")
    else:
        print("Exclusão cancelada!")

# Função de editar o cadastro de um atleta
def editar_cadastro(nome_atleta, opcao_edicao, atletas):
    atleta = atletas[nome_atleta]
    try:
        # Editar o nome do atleta
        if opcao_edicao == 1:
            print(f"Nome cadastrado: {atleta.nome}")
            atleta.nome = validar_nome_utilizado(input("Digite o novo nome do atleta:\n").title(), atletas)
            del atletas[nome_atleta]
            atletas[atleta.nome] = atleta
        # Editar a idade do atleta
        elif opcao_edicao == 2:
            print(f"Idade cadastrada: {atleta.idade}")
            atleta.idade = input("Digite a nova idade do atleta:\n")
        # Editar o sexo do atleta
        elif opcao_edicao == 3:
            print("Sexo cadastrado:", "Feminino" if atleta.sexo == "f" else "Masculino")
            atleta.sexo = input("Digite o novo sexo do atleta [M] ou [F]:\n").lower()
        # Editar a paralisia do atleta
        elif opcao_edicao == 4:
            print(f"Paralisia cadastrada: {atleta.paralisia}")
            atleta.paralisia = input("Digite o novo tipo de parisilia do atleta:\n")
        # Editar o diagnostico de COVID do atleta
        elif opcao_edicao == 5:
            print(f"Diagnostico cadastrado:", "Positivo" if atleta.covid else "Negativo")
            atleta.covid = input("Digite o novo diagnostico de COVID-19 do atleta [S] ou [N]:\n").lower()
        # Editar a modalidade do atleta
        elif opcao_edicao == 6:
            modalidade = (atleta.modalidade).name.title().replace("_", " ")
            print(f"Modalidade cadastrada: {modalidade}")
            listar_modalidades()
            atleta.modalidade = input("Digite a nova modalidade do atleta:\n")
        # Editar as medalhas do atleta
        elif opcao_edicao == 7:
            print(f"Medalhas cadastradas: \nOuro - {atleta.medalhas[0]}\nPrata - {atleta.medalhas[1]}\nBronze - {atleta.medalhas[2]}")
            print("Digite as novas medalhas do atleta:")
            atleta.medalhas = qtd_medalhas("s")
        print("Edição feita com sucesso!")
    except Exception as excep:
        print(excep)

# Função que chama as funções responsáveis pelos relátorios de acordo com a escolha do usuário
def imprimir_relatorio(opcao_relatorio,atletas):
    # 1 - A quantidade de atletas que participaram dos jogos separados por modalidade e sexo
    if opcao_relatorio == 1:
        qtd_masc_modalidades, qtd_fem_modalidades, total_geral_qtd = qtd_atletas_modalidade(atletas)
        formatar_qtd_atletas_modalidade(qtd_masc_modalidades, qtd_fem_modalidades, total_geral_qtd)
    # 2 - Relação dos atletas diagnosticados com Covid-19 separados por modalidade e sexo
    elif opcao_relatorio == 2:
        covid_fem_modalidades, covid_masc_modalidades, total_geral_covid = atletas_covid_modalidades(atletas)
        formatar_atletas_covid_modalidades(covid_masc_modalidades, covid_fem_modalidades, total_geral_covid)
    # 3 - Quadro de medalhas
    elif opcao_relatorio == 3:
        medalhas = quadro_medalhas(atletas)
        imprimir_quadro_medalhas(medalhas)
    # 4 - Dados dos atletas que conquistaram medalhas
    elif opcao_relatorio == 4:
        medalha_masc_modalidades, medalha_fem_modalidades, atletas_masc, atletas_fem = atletas_ganharam_medalhas(atletas)
        formatar_atletas_ganharam_medalhas(medalha_masc_modalidades, medalha_fem_modalidades, atletas_masc, atletas_fem)
    # 5 - Relatório de Modalidades (Brasil)
    elif opcao_relatorio == 5:
        participacao_brasil(atletas)
    # 6 - Todas opções acima
    elif opcao_relatorio == 6:
        qtd_masc_modalidades, qtd_fem_modalidades, total_geral_qtd = qtd_atletas_modalidade(atletas)
        formatar_qtd_atletas_modalidade(qtd_masc_modalidades, qtd_fem_modalidades, total_geral_qtd)
        covid_fem_modalidades, covid_masc_modalidades, total_geral_covid = atletas_covid_modalidades(atletas)
        formatar_atletas_covid_modalidades(covid_masc_modalidades, covid_fem_modalidades, total_geral_covid)
        medalhas = quadro_medalhas(atletas)
        imprimir_quadro_medalhas(medalhas)
        medalha_masc_modalidades, medalha_fem_modalidades, atletas_masc, atletas_fem = atletas_ganharam_medalhas(atletas)
        formatar_atletas_ganharam_medalhas(medalha_masc_modalidades, medalha_fem_modalidades, atletas_masc, atletas_fem)
        participacao_brasil(atletas)

# Função que mostra uma lista com o nome de todos os atletas cadastrados
def listar_nome_atletas(atletas):
    print("Lista de atletas cadastrados: ")
    for i,nome in enumerate(sorted(atletas.keys())):
        print(f"{i} - {nome}")

# Função que mostra uma lista com o nome de todas as modalidades
def listar_modalidades():
    print("Lista de Modalidades:")
    for modalidade in Modalidades:
        print(modalidade.value, "-" ,(modalidade.name).title().replace("_", " "))

#1) A quantidade total de atletas que participaram dos Jogos Paraolímpicos por modalidade e sexo, informando também o total geral;
def qtd_atletas_modalidade(atletas):
    qtd_masc_modalidades = [0 for i in range(22)]
    qtd_fem_modalidades = [0 for i in range(22)]
    total_geral = [0 for i in range(22)]
    for atleta in atletas.values():
        if atleta.sexo == "f":
            qtd_fem_modalidades[atleta.modalidade.value] += 1
        else:
            qtd_masc_modalidades[atleta.modalidade.value] += 1
        total_geral[atleta.modalidade.value] += 1
    return qtd_masc_modalidades, qtd_fem_modalidades, total_geral

# Função que organiza as informações do relatório 1
def formatar_qtd_atletas_modalidade(qtd_masc_modalidades, qtd_fem_modalidades, total_geral_qtd):
    print(f"Quantidade total de atletas que participaram dos Jogos Paraolímpicos: {sum(total_geral_qtd)}")
    imprimir_qtd_atletas(total_geral_qtd)
    print(f"\nQuantidade de atletas do sexo Masculino: {sum(qtd_masc_modalidades)}")
    imprimir_qtd_atletas(qtd_masc_modalidades)
    print(f"\nQuantidade de atletas do sexo Feminino: {sum(qtd_fem_modalidades)}")
    imprimir_qtd_atletas(qtd_fem_modalidades)

# Função que imprime as imprime a quantidade de atletas de cada modalidade usada na relatório 1 e 2
def imprimir_qtd_atletas(lista):
    for index, modalidade in enumerate(lista):
        if modalidade > 0:
            print(Modalidades(index).name.title().replace("_", " ") + f": {modalidade} atletas")

#2) Relação dos atletas diagnosticados com Covid-19 por modalidade e sexo;
def atletas_covid_modalidades(atletas):
    covid_fem_modalidades = [0 for i in range(22)]
    covid_masc_modalidades = [0 for i in range(22)]
    total_geral = [0 for i in range(22)]
    for atleta in atletas.values():
        if atleta.covid:
            if atleta.sexo == "f":
                covid_fem_modalidades[atleta.modalidade.value] += 1
            else:
                covid_masc_modalidades[atleta.modalidade.value] += 1
            total_geral[atleta.modalidade.value] += 1
    return covid_fem_modalidades, covid_masc_modalidades, total_geral

# Função que organiza as informações do relatório 2
def formatar_atletas_covid_modalidades(covid_masc_modalidades, covid_fem_modalidades, total_geral_covid):
    print(f"Quantidade total de atletas que foram diagnosticados com COVID-19: {sum(total_geral_covid)}")
    print(f"\nQuantidade de atletas do sexo Masculino: {sum(covid_masc_modalidades)}")
    imprimir_qtd_atletas(covid_masc_modalidades)
    print(f"\nQuantidade de atletas do sexo Feminino: {sum(covid_fem_modalidades)}")
    imprimir_qtd_atletas(covid_fem_modalidades)

#3) Quadro de medalhas: quantitativo de medalhas de ouro, prata e bronze por modalidade, ordenadas primeiramente 
#   pelo número de medalhas de ouro, seguidas pelo número de medalhas de prata, finalmente, de bronze;
def quadro_medalhas(atletas):
    medalhas = [[0 for i in range(3)] for i in range(22)]
    for atleta in atletas.values():
        index = atleta.modalidade.value
        for i, medalha in enumerate(atleta.medalhas):
            medalhas[index][i] += medalha
    return medalhas

# Função que imprime o quadro de medalhas do relatório 3
def imprimir_quadro_medalhas(medalhas):
    print("Quadro de medalhas por modalidade:")
    for i in range(22):
        if sum(medalhas[i]) > 0:
            print(Modalidades(i).name.title().replace("_", " ") + ":")
            print(f"Ouro - {medalhas[i][0]}\nPrata - {medalhas[i][1]}\nBronze - {medalhas[i][2]}")

#4) Um recorte por modalidade e por gênero (M/F) dos atletas que ganharam medalhas, com a informação do nome do atleta, idade, tipo de paralisia e medalha(s) conquistada(s).
def atletas_ganharam_medalhas(atletas):
    medalha_masc_modalidades = [[]for i in range(22)]
    medalha_fem_modalidades = [[]for i in range(22)]
    atletas_masc = 0
    atletas_fem = 0
    for atleta in atletas.values():
        if atleta.medalhas[0] > 0 or atleta.medalhas[1] > 0 or atleta.medalhas[2] > 0:
            if atleta.sexo == "f":
                medalha_fem_modalidades[atleta.modalidade.value].append(atleta)
                atletas_fem += 1
            else:
                medalha_masc_modalidades[atleta.modalidade.value].append(atleta)
                atletas_masc += 1
    return medalha_masc_modalidades, medalha_fem_modalidades, atletas_masc, atletas_fem

# Função que organiza as informações do relatório 4
def formatar_atletas_ganharam_medalhas(medalha_masc_modalidades, medalha_fem_modalidades, atletas_masc, atletas_fem):
    if atletas_masc > 0:
        print("Atletas que receberam medalhas do sexo Masculino:")
        imprimir_atletas_ganharam_medalhas(medalha_masc_modalidades)
    if atletas_fem > 0:
        print("\nAtletas que receberam medalhas do sexo Feminino:")
        imprimir_atletas_ganharam_medalhas(medalha_fem_modalidades)

# Funçao que imprime os dados dos atletas que ganharam medalhas separado por modalidade usada no relatório 4
def imprimir_atletas_ganharam_medalhas(lista):
    for index, modalidade in enumerate(lista):
        num_atleta = 1
        if len(modalidade) > 0:
            print("\n" + Modalidades(index).name.title().replace("_", " ") + ":")
            for atleta in modalidade:
                print(f"\n- Atleta {num_atleta}")
                print(atleta)
                num_atleta += 1

# 5) Das 22 modalidades disponíveis nos Jogos Paralímpicos de Tóquio, quantas o Brasil teve participação? Em quais modalidades ganhou medalha(s)? Quais modalidades 
# que o Brasil participou e não ganhou medalha(s)? Quantas e quais modalidades o Brasil não participou? Apresentar as modalidades em ordem alfabética.
def participacao_brasil(atletas):
    qtd_participou = 0 # Quantidade de modalidades que o Brasil participou
    nao_participou = [] # Nome das modalidades que o Brasil não participou
    ganhou_medalha = [] # Nome das modalidades que o Brasil ganhou medalhas
    nao_ganhou_medalha = [] # Nome das modalidades que o Brasil participou mas não ganhou medalhas

    qtd_masc_modalidades, qtd_fem_modalidades, total_geral_qtd = qtd_atletas_modalidade(atletas)
    medalhas = quadro_medalhas(atletas)

    for j, modalidade in enumerate(total_geral_qtd):
        if modalidade > 0:
            qtd_participou += 1
        else:
            nao_participou.append(Modalidades(j).name.title().replace("_", " "))

    qtd_nao_participou = 22 - qtd_participou # Quantidade de modalidades que o Brasil não participou

    for i, modalidade in enumerate(medalhas):
        if sum(modalidade) > 0:
            ganhou_medalha.append(Modalidades(i).name.title().replace("_", " "))
        else:
            if total_geral_qtd[i] > 0:
                nao_ganhou_medalha.append(Modalidades(i).name.title().replace("_", " "))

    print(f"O Brasil participou de {qtd_participou} das 22 modalidades disponíveis")
    print("\nGanhou medalha nas modalidades:")
    for modalidade in ganhou_medalha:
        print(f"- {modalidade}")
    print("\nNão ganhou medalhas nas modalidades:")
    for modalidade in nao_ganhou_medalha:
        print(f"- {modalidade}")

    print(f"\nO Brasil não participou de {qtd_nao_participou} modalidades, sendo elas:")
    for modalidade in nao_participou:
        print(f"- {modalidade}")

# Função que valida se a resposta para medalhas é S ou N
def validar_medalhas(opcao):
    lista_medalhas = ["0" for i in range(3)]
    while not (opcao == "s" or opcao == "n"):
        print("Opção Inválida! Responda com [S] para Sim ou [N] para Não")
        opcao = input("O atleta recebeu alguma medalha? [S] ou [N]\n").lower()
    # Se o atleta tiver ganhado medalhas, é perguntado a quantidade
    if opcao == "s":
       lista_medalhas = qtd_medalhas(lista_medalhas)
    # Se o atleta não tiver ganhado medalhas, é retorna uma lista com 3 zeros
    return lista_medalhas

# Função que pergunta quantas medalhas o atleta ganhou
def qtd_medalhas(lista_medalhas):
    quantidade_ouro = input("Quantas medalhas de Ouro o atleta recebeu?\n")
    lista_medalhas[0] = quantidade_ouro
    quantidade_prata = input("Quantas medalhas de Prata o atleta recebeu?\n")
    lista_medalhas[1] = quantidade_prata
    quantidade_bronze = input("Quantas medalhas de Bronze o atleta recebeu?\n")
    lista_medalhas[2] = quantidade_bronze
    return lista_medalhas

# Função que recebe os dados do atleta para realizar o cadastro
def entradas(atletas):
    atleta = None
    while atleta is None: # Enquanto um cadastro não for realizado, as entradas são pedidas novamente
        nome = validar_nome_utilizado(input("Digite o nome do atleta:\n").title(), atletas)
        idade = input("Digite a idade do atleta:\n")
        sexo = input("Digite o sexo do atleta [M] ou [F]:\n").lower()
        paralisia = input("Digite o tipo de parisilia do atleta:\n")
        covid = input("O atleta foi diagnosticado com COVID-19? [S] ou [N]\n").lower()
        listar_modalidades()
        modalidade_atleta = input("Digite a modalidade do atleta:\n")
        medalhas = validar_medalhas(input("O atleta recebeu alguma medalha? [S] ou [N]\n").lower())
        try:
            atleta = Atleta(nome,sexo,idade,modalidade_atleta,medalhas,paralisia,covid)
            atletas[atleta.nome] = atleta
            print("Atleta cadastrado com sucesso!")
        except Exception as excep:
            print(excep)

# Função que valida a opção escolhida no menu
def escolha_menu():
    opcao = input("Digite a opção que deseja selecionar: ")
    while not opcao.isdigit() or int(opcao) < 0 or int(opcao) > 6:
        print("Opção Inválida!")
        opcao = input("Digite a opção que deseja selecionar: ")
    return int(opcao)

# Função que valida a opção escolhida no menu de edição de cadastro
def validar_menu_edicao(value):
    while not value.isdigit() or int(value) < 0 or int(value) > 8:
        print("Opção Inválida!")
        value = input("Digite a opção que deseja selecionar: ")
    return int(value)

# Função que valida a opção escolhida no menu de relatórios
def validar_menu_relatorio(value):
    while not value.isdigit() or int(value) < 0 or int(value) > 7:
        print("Opção Inválida!")
        value = input("Digite a opção que deseja selecionar: ")
    return int(value)

# Função que valida se a resposta dada é S ou N
def validar_sim_nao(opcao):
    while not (opcao == "s" or opcao == "n"):
        opcao = input("Responda com [S] ou [N]:\n").lower()
    return opcao

# Função que valida se o nome do atleta já está cadastrado para impedir duplicidade
def validar_nome_utilizado(nome,atletas):
    while nome in atletas.keys() or nome == "Sair":
        if nome == "Sair":
            print("Não é possível cadastrar um atleta com esse nome")
            nome = input("Digite outro nome:\n").title()
        else:
            nome = input("Atleta já cadastrado digite outro nome:\n").title()
    return nome

# Função que valida se o nome do atleta já está cadastrado
def validar_nome_existe(nome, atletas):
    while nome not in atletas.keys() and nome != "Sair":
        nome = input("Atleta não cadastrado digite outro nome: ").title()
    return nome

# Função que redireciona a opção escolhida no menu para outras funções
def opcoes_menu(opcao,atletas):
    while opcao != 6:
        # Cadastrar um atleta
        if opcao == 1:
            print(tela_cabecalho_cadastro())
            entradas(atletas)
            continuar = validar_sim_nao(input("Deseja cadastrar outro atleta? [S] ou [N]\n").lower())
            while continuar == "s":
                escrever_arquivo(atletas)
                entradas(atletas)
                continuar = validar_sim_nao(input("Deseja cadastrar outro atleta? [S] ou [N]\n").lower())
            print("Cadastro Finalizado!")
        # Editar o cadastro de um atleta
        elif opcao == 2:
            print(tela_menu_edicao())
            opcao_edicao = validar_menu_edicao(input("Digite a opção que deseja selecionar: "))
            if opcao_edicao != 8:
                print(tela_cabecalho_edicao())
                listar_nome_atletas(atletas)
                nome_atleta = validar_nome_existe(input("[SAIR] Para voltar para o menu\nDigite o nome do atleta que deseja editar: ").title(), atletas)
                if nome_atleta != "Sair":
                    editar_cadastro(nome_atleta,opcao_edicao,atletas)
        # Deletar o cadastro de um atleta
        elif opcao == 3:
            print(tela_cabecalho_excluir())
            listar_nome_atletas(atletas)
            nome_atleta = validar_nome_existe(input("[SAIR] Para voltar para o menu\nDigite o nome do atleta que deseja excluir: ").title(), atletas)
            if nome_atleta != "Sair":
                deletar_atleta(nome_atleta, atletas)       
        # Visualizar o cadastro de um atleta
        elif opcao == 4:
            print(tela_cabecalho_dados())
            listar_nome_atletas(atletas)
            nome_atleta = validar_nome_existe(input("[SAIR] Para voltar para o menu\nDigite o nome do atleta que deseja visualizar: ").title(), atletas)
            if nome_atleta != "Sair":
                print(f"\n{atletas[nome_atleta]}")
        # Ver os relatórios
        else:
            print(tela_menu_relatorio())
            opcao_relatorio = validar_menu_relatorio(input("Digite a opção que deseja selecionar: "))
            imprimir_relatorio(opcao_relatorio, atletas)
        escrever_arquivo(atletas)
        print(tela_menu())
        opcao = escolha_menu()

# Função que lê os atletas cadastrados em um arquivo e adiciona ao sistema
def ler_arquivo():
    atletas = {}
    nome_arquivo = "lista_atletas.json"
    if os.path.exists(nome_arquivo):
        try:
            arquivo = open(nome_arquivo, "r")
            atletas = jsonpickle.decode(arquivo.read())
            arquivo.close()
        except:
            print("Não foi possível ler os dados do arquivo salvo!")
    return atletas

# Função que grava os cadastros dos atletas em um arquivo
def escrever_arquivo(atletas):
    nome_arquivo = "lista_atletas.json"
    arquivo = open(nome_arquivo, "w")
    arquivo.write(jsonpickle.encode(atletas))
    arquivo.close()

def main():
    atletas = ler_arquivo()
    print(tela_apresentacao())
    print(tela_menu())
    opcao = escolha_menu()
    opcoes_menu(opcao, atletas)

if __name__ =="__main__":
    main()
