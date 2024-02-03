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
from functions import *
menu()
opcao = validar_escolha_menu(input("   Digite a opção que deseja selecionar: "))
print()

# Enquanto o jogador não escolher sair o menu é apresentado
while opcao != 3:
    pontuacao = 0 # Variável para acumular a pontuação
    tabuleiro_valido = False

    if opcao == 1:
        linhas, colunas, cores = escolher_tabuleiro()
        # Enquanto o tabuleiro não possuir jogadas válidas é gerado um novo
        while not tabuleiro_valido:    
            tabuleiro = gerar_tabuleiro(linhas, colunas, cores)
            qnt_quebradas = quebrar_gemas(tabuleiro)
            # Enquanto gemas forem quebradas o tabuleiro é ciclado
            while qnt_quebradas > 0:
                gravidade(tabuleiro)
                gerar_novas_gemas(tabuleiro, cores)
                qnt_quebradas = quebrar_gemas(tabuleiro)

            tabuleiro_valido = verificar_movimentos_validos(tabuleiro)
        # Enquanto houver movimentos no tabuleiro o jogador pode escolher a ação que deseja realizar
        while verificar_movimentos_validos(tabuleiro):
            print()
            imprimir_tabuleiro(tabuleiro)
            print(f"Pontuação: {pontuacao}\n")
            # Pergunta o jogador a ação que ele deseja realizar
            escolha = validar_digitos(input('Escolha uma ação:\n1) Mover Gemas\n2) Dica\n3) Sair\n'))
            print()
            if escolha == 1:
                linha1, coluna1, linha2, coluna2 = escolher_permuta_gemas()
                if validar_permuta(linha1, coluna1, linha2, coluna2, tabuleiro):
                    permutar_gemas(linha1, coluna1, linha2, coluna2, tabuleiro)
                    qnt_quebradas = quebrar_gemas(tabuleiro)
                    # Se após gerar novas gemas houver permutas as gemas serão quebradas automaticamente
                    while qnt_quebradas > 0:
                        gravidade(tabuleiro)
                        gerar_novas_gemas(tabuleiro, cores)
                        pontuacao += qnt_quebradas
                        qnt_quebradas = quebrar_gemas(tabuleiro)
            elif escolha == 2:
                # Se o jogador possuir mais de 1 ponto a dica é apresentada
                if pontuacao > 0:
                    pontuacao -= 1
                    i, j, x = pedir_dica(tabuleiro)
                    imprimir_dica(i,j,x)
                # Se o jogador não possuir ao menos 1 ponto ele não pode pedir dica
                else:
                    print("+-----------------------------------+")
                    print("|  Você não tem pontos suficiente!  |")
                    print("+-----------------------------------+")
            elif escolha == 3:
                # Se o jogador escolher sair a pontuação dele é mostrada e o jogo encerrado
                game_over(pontuacao)
                input("          Pressione ENTER para Sair\n")
                exit()
            else:
                print("+-------------------+")
                print("|  Opção Inválida!  |")
                print("+-------------------+")
        # Quando não houver mais movimentos o jogo é encerrado
        game_over(pontuacao)
        print("           Acabaram os movimentos!            ")
        print("              ▄    ▄▄▄▄▄▄▄    ▄               ")
        print("             ▀▀▄ ▄█████████▄ ▄▀▀              ")
        print("                 ██ ▀███▀ ██                  ")
        print("               ▄ ▀████▀████▀ ▄                ")
        print("             ▀█    ██▀█▀██    █▀              ")
        print()
        input("   Pressione ENTER para voltar para o Menu  \n")
    else:
        tutorial()
    menu()
    opcao = validar_escolha_menu(input("   Digite a opção que deseja selecionar: "))
    print()
exit()