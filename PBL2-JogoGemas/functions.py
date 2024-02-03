'''/*******************************************************************************
Autor: João Victor Alves Cerqueira
Componente Curricular: MI - Algoritmos (TP04)
Concluido em: 14/10/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''
from random import choice
import string
# Função que mostra a tela do menu
def menu():
    print("+--------------------------------------------+")
    print("|    ██████╗ ███████╗███╗   ███╗ ██████╗     |")
    print("|   ██╔════╝ ██╔════╝████╗ ████║██╔════╝     |")
    print("|   ██║  ██╗ █████╗  ██╔████╔██║╚█████╗      |")
    print("|   ██║  ╚██╗██╔══╝  ██║╚██╔╝██║ ╚═══██╗     |")
    print("|   ╚██████╔╝███████╗██║ ╚═╝ ██║██████╔╝     |")
    print("|    ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═════╝      |")
    print("+--------------------------------------------+")
    print(" *      *     +--------------+  *          *  ")
    print("            * | (1) Jogar    |        *       ")
    print("*    *        | (2) Tutorial |    *          *")
    print("          *   | (3) Sair     |          *     ")
    print("    *         +--------------+   *          * ")
    print("*        *           *       *          *     ")

# Função que mostra a tela de tutorial
def tutorial():
    print("+--------------------------------------------+")
    print("|        ▀█▀ █ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █         |")
    print("|         █  █▄█  █  █▄█ █▀▄ █ █▀█ █▄▄       |")
    print("+--------------------------------------------+")
    print("   1) Escolha o número de linhas e colunas    ")
    print("    do tabuleiro, e a quantidade de cores     ")
    print("              que deseja jogar.               ")
    print("  2) Após o tabuleiro ser apresentado você    ")
    print("      deverá escolher se deseja fazer um      ")
    print("        movimento ou pedir uma dica.          ")
    print("  3) Para fazer um movimento digite a posição ")
    print("        da gema de acordo solicitado.         ")
    print(" 4) Se o movimento for válido, você receberá  ")
    print("   os pontos de acordo a quantidade de gemas  ")
    print("                 quebradas.                   ")
    print("         5) Repita os passos 2 - 4.           ")
    print()
    print("         Obs: As dicas custam 1 ponto         ")
    print()
    input("   Pressione ENTER para voltar para o Menu  \n")

# Função que mostra a tela de final do jogo
def game_over(pontos):
    print("+--------------------------------------------+")
    print("|     █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █ █ █▀▀ █▀█    |")
    print("|     █▄█ █▀█ █ ▀ █ ██▄   █▄█ ▀▄▀ ██▄ █▀▄    |")
    print("+--------------------------------------------+")
    print(f"              Você fez {pontos} pontos!      ")

def imprimir_dica(i,j,x):
    print("+--------------------------------------------+")
    print("|*    *    *    █▀▄ █ █▀▀ ▄▀█     *     *    |")
    print("|  *     *   *  █▄▀ █ █▄▄ █▀█   *     *    * |")
    print("+--------------------------------------------+")
    if x == -2:
        print(f"     Mova a gema [{i}][{j}] com a gema [{i}][{j + 1}]")
    else:
        print(f"     Mova a gema [{i}][{j}] com a gema [{i + 1}][{j}]")

# Função para validar a escolha do menu(Se é número e se a opção selecionada existe)
def validar_escolha_menu(opcao):
    while not opcao.isdigit() or int(opcao) < 1 or int(opcao) > 3:
        print("             Opção Inválida!             ")
        opcao = input("   Digite a opção que deseja selecionar: ")
    return int(opcao)

# Função para escolher a quantidade de linhas, colunas e cores do tabuleiro
def escolher_tabuleiro():
    linhas = validar_num_linhas_colunas(input("Digite o número de linhas do tabuleiro [3 - 10]: "))
    colunas = validar_num_linhas_colunas(input("Digite o número de colunas do tabuleiro [3 - 10]: "))
    cores = validar_num_cores(input("Digite a quantidade de cores das gemas [3 - 26]: "))
    return linhas, colunas, cores

# Função para validar se o que foi digitado é número
def validar_digitos(num):
    while not num.isdigit():
        num = input("Utilize somente números: ")
    return int(num)

# Função para validar se a quantidade de linhas e colunas está dentro do permitido(Maior que 3 e menor que 10)
def validar_num_linhas_colunas(num):
    while not num.isdigit() or int(num) < 3 or int(num) > 10:
        print("Valor Inválido!")
        num = input("Digite um valor entre 3 e 10: ")
    return int(num)

# Função para validar se a quantidade de cores escolhidas é válida(Maior que 3 e menor que 26)
def validar_num_cores(num):
    while not num.isdigit() or int(num) < 3 or int(num) > 26:
        print("Valor Inválido!")
        num = input("Digite um valor entre 3 e 26: ")
    return int(num)

# Função que gera o tabuleiro
def gerar_tabuleiro(num_linhas, num_colunas, num_cores):
    tabuleiro = [[choice(list(string.ascii_uppercase)[0:num_cores]) for colunas in range(num_colunas)]for linhas in range(num_linhas)]
    return tabuleiro

# Função que imprime o tabuleiro na tela
def imprimir_tabuleiro(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])

    for x in range(num_colunas):
        if x == 0:
            print("    ", end = "")
        print(x, end = " ")
    print()
    
    for x in range(num_colunas):
        if x == 0:
            print("  +-", end = "")
        print("--", end = "")
    print("+")

    for i in range(num_linhas):
        print(i, end = " | ")
        for j in range(num_colunas):
            print(tabuleiro[i][j], end=" ")
        print("|")

    for x in range(num_colunas):
        if x == 0:
            print("  +-", end = "")
        print("--", end = "")
    print("+")
    print()

# Função que valida se existem cadeias na horizontal
# Trecho de código base elaborado na sessão do dia 23/09/2021
def validar_cadeia_horizontal(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for i in range(num_linhas):
        contador = 1
        for j in range(num_colunas - 1):
            if (tabuleiro[i][j]).lower() == (tabuleiro[i][j + 1]).lower():
                contador += 1
            else:
                contador = 1
            # Quando o contador é maior ou igual a 3 existe ao menos uma cadeia na horizontal
            if contador >= 3:
                return True
    return False

# Função que valida se existem cadeias na vertical
# Trecho de código base elaborado na sessão do dia 23/09/2021
def validar_cadeia_vertical(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for j in range(num_colunas):
        contador = 1
        for i in range(num_linhas - 1):
            if (tabuleiro[i][j]).lower() == (tabuleiro[i + 1][j]).lower():
                contador += 1
            else:
                contador = 1
            # Quando o contador é maior ou igual a 3 existe ao menos uma cadeia na vertical
            if contador >= 3:
                return True
    return False

# Função que transforma as cadeias formadas na horizontal em letras minúculas
# Trecho de código base elaborado na sessão do dia 23/09/2021
def quebrar_cadeia_horizontal(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for i in range(num_linhas):
        contador = 1
        for j in range(num_colunas - 1):
            if (tabuleiro[i][j]).lower() == (tabuleiro[i][j + 1]).lower():
                contador += 1
            else:
                contador = 1
            # Quando o contador é maior ou igual a 3 existe uma quebra e as letras ão substituidas por letras minúculas
            if contador >= 3:
                k = j + 1
                while k > j + 1 - contador:
                    if tabuleiro[i][k].isupper():
                        tabuleiro[i][k] = tabuleiro[i][k].lower()
                    k -= 1

# Função que transforma as cadeias formadas na vertical em letras minúculas
# Trecho de código base elaborado na sessão do dia 23/09/2021
def quebrar_cadeia_vertical(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for j in range(num_colunas):
        contador = 1
        for i in range(num_linhas - 1):
            if (tabuleiro[i][j]).lower() == (tabuleiro[i + 1][j]).lower():
                contador += 1
            else:
                contador = 1
            # Quando o contador é maior ou igual a 3 existe uma quebra e as letras ão substituidas por letras minúculas
            if contador >= 3:
                k = i + 1
                while k > i + 1 - contador:
                    if tabuleiro[k][j].isupper():
                        tabuleiro[k][j] = tabuleiro[k][j].lower()
                    k -= 1

# Função que transforma as letras mínusculas do tabuleiro em * (espaços vazios)
def quebrar_gemas(tabuleiro):
    qnt_quebradas = 0
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    quebrar_cadeia_horizontal(tabuleiro)
    quebrar_cadeia_vertical(tabuleiro)
    for i in range(num_linhas):
        for j in range(num_colunas):
            if tabuleiro[i][j].islower():
                tabuleiro[i][j] = "*"
                qnt_quebradas += 1
    return qnt_quebradas

# Função que substitui os * (espaços vazios) criados na função quebrar_gemas por novas letras
def gerar_novas_gemas(tabuleiro, num_cores):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            if tabuleiro[i][j] == "*":
                tabuleiro[i][j] = choice(list(string.ascii_uppercase)[0:num_cores])

# Função com inputs utilizados para o jogador escolher as gemas que deseja permutar
def escolher_permuta_gemas():
    linha_gema1 = validar_digitos(input("Digite a linha da primeira gema: "))
    coluna_gema1 =  validar_digitos(input("Digite a coluna da primeira gema: "))
    linha_gema2 = validar_digitos(input("Digite a linha da segunda gema: "))
    coluna_gema2 =  validar_digitos(input("Digite a coluna da segunda gema: "))
    return linha_gema1, coluna_gema1, linha_gema2, coluna_gema2

# Função que verifica se a permuta feita é válida
def validar_permuta(linha1, coluna1, linha2, coluna2, tabuleiro):
    num_linhas = len(tabuleiro) - 1
    num_colunas = len(tabuleiro[0]) - 1
    # Verifica se a posição escolhida está dentro do limite do tabuleiro
    if linha1 > num_linhas or linha2 > num_linhas or linha1 < 0  or linha2 < 0 or coluna1 > num_colunas or coluna2 > num_colunas or coluna1 < 0 or coluna2 < 0:
        print("+---------------------+")
        print("|  Posição Inválida!  |")
        print("+---------------------+")
        return False
    # Verifica se a posição das gemas tem a diferença absoluta de 1 posição(-1 para cima, 1 para baixo, -1 para esquerda, 1 para direita)
    # Trecho de código retirado da sessão MI
    if not ((linha1 == linha2 and abs(coluna1 - coluna2) == 1) or (coluna1 == coluna2 and abs(linha1 - linha2) == 1)):
        print("+----------------------+")
        print("|  Movimento inválido  |")
        print("+----------------------+")
        return False
    return True

# Se a permuta realizada passar pela função validar_permuta a permuta é realizada
def permutar_gemas(linha1, coluna1, linha2, coluna2, tabuleiro):
    tabuleiro[linha1][coluna1],tabuleiro[linha2][coluna2] = tabuleiro[linha2][coluna2], tabuleiro[linha1][coluna1]
    # É chamada a função para validar se a permuta realizada gerou quebra
    if validar_cadeia_vertical(tabuleiro) or validar_cadeia_horizontal(tabuleiro):
        # Se a permuta gerar quebra a permuta é válida
        return True
    # Se a permuta não for válida ela é desfeita
    else:
        tabuleiro[linha1][coluna1],tabuleiro[linha2][coluna2] = tabuleiro[linha2][coluna2], tabuleiro[linha1][coluna1]
        print("+-------------------------------+")
        print("|  Nenhuma gema foi destruida   |")
        print("|      Movimento Desfeito!      |")
        print("+-------------------------------+")
        return False

# Função que faz as gemas cairem caso houver espaços vazios embaixo delas
# Trecho de código apresentado por Ian Gabriel na sessão do dia 30/09/2021
def gravidade(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for d in range(num_linhas):
        for i in range(num_linhas - 1, 0 ,-1):
            for j in range(num_colunas - 1, -1, -1):
                if tabuleiro[i][j] == "*":
                    tabuleiro[i][j], tabuleiro[i - 1][j] = tabuleiro[i - 1][j], tabuleiro[i][j]

# Função responsável por dar as dicas do jogo
def pedir_dica(tabuleiro):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    # Procura permutas na horizontal
    for i in range(num_linhas):
        for j in range(num_colunas - 1):
            # Faz a substituição das gemas
            tabuleiro[i][j], tabuleiro[i][j + 1] = tabuleiro[i][j + 1],tabuleiro[i][j]
            # Verifica se com a substituição realizada existe uma quebra
            if validar_cadeia_vertical(tabuleiro) or validar_cadeia_horizontal(tabuleiro):
                # A substiuição é desfeita
                tabuleiro[i][j], tabuleiro[i][j + 1] = tabuleiro[i][j + 1],tabuleiro[i][j]
                # Se uma quebra ocorrer é passada a posição da gema que se deve movimentar
                return i, j, -2
            # Se não houver quebra a substiuição é desfeita
            tabuleiro[i][j], tabuleiro[i][j + 1] = tabuleiro[i][j + 1],tabuleiro[i][j]
    # Se não houver permutas na horizontal, são procuradas permutas na vertical
    for j in range(num_colunas):
        for i in range(num_linhas - 1):
            # Faz a substituição das gemas
            tabuleiro[i][j],tabuleiro[i + 1][j] = tabuleiro[i + 1][j], tabuleiro[i][j]
            # Verifica se com a substituição realizada existe uma quebra
            if validar_cadeia_vertical(tabuleiro) or validar_cadeia_horizontal(tabuleiro):
                # A substiuição é desfeita
                tabuleiro[i][j],tabuleiro[i + 1][j] = tabuleiro[i + 1][j], tabuleiro[i][j]
                # Se uma quebra ocorrer é passada a posição da gema que se deve movimentar
                return i, j, -1
            # Se não houver quebra a substiuição é desfeita
            tabuleiro[i][j],tabuleiro[i + 1][j] = tabuleiro[i + 1][j], tabuleiro[i][j]
    # Se não houver nenhuma dica é retornado o valor 11
    return 11, 11, 11
            
# Função que verifica se ainda existem movimentos no tabuleiro
def verificar_movimentos_validos(tabuleiro):
    i, j, x = pedir_dica(tabuleiro)
    # Se as variáveis i, j e x possuirem o valor 11 é porque não existem mais jogadas
    if i == 11 and j == 11 and x == 11:
        return False
    # Se for recebido qualquer outro valor ainda existem jogadas que possam ser feitas
    return True