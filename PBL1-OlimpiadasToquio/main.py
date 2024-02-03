'''/*******************************************************************************
Autor: João Victor Alves Cerqueira
Componente Curricular: MI - Algoritmos (TP04)
Concluido em: 05/09/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''
# Variáveis para idades
qntIdades = somaIdadeGeral = idadeMaisVelho = idadeMaisNovo = qntIdadesComSintomas = qntIdadesSemSintomas = somaIdadeComSintomas = somaIdadeSemSintomas = 0
# Variáveis para quantidade de atletas que tiveram sintomas
sintoma = qntSintomas = 0
# Variáveis para número de atletas dos sexo masculino e feminino
atletasM = atletasF = 0
# Variáveis para temperatura máxima de febre alcançada
temperaturaMAX = temperatura = 0
# Variáveis para Kit COVID
atletasFKitSintoma = atletasMKitSintoma = atletasFKitSemSintoma = atletasMKitSemSintoma = 0
# Variáveis para calculo de idade média
idadeMediaSemSintomas = idadeMediaComSintomas = 0
# Variáveis para medalhas [Homem/Sintomático]
somaOuroMascComSintoma = somaPrataMascComSintoma = somaBronzeMascComSintoma = 0
# Variáveis para medalhas [Mulher/Sintomático]
somaOuroFemComSintoma = somaPrataFemComSintoma = somaBronzeFemComSintoma = 0
# Variáveis para medalhas [Homem/Assintomático]
somaOuroMascSemSintoma = somaPrataMascSemSintoma = somaBronzeMascSemSintoma = 0
# Variáveis para medalhas [Mulher/Assintomático]
somaOuroFemSemSintoma = somaPrataFemSemSintoma = somaBronzeFemSemSintoma = 0
# Variável para cadastro de novo atleta
cadastro = "s"

print("\t\t     Bem-vindo(a) ao sistema UEFS pelos Atletas")
print("|Um programa criado por alunos da UEFS em parceria com o Comitê Olímpico Brasileiro|\n")
print(f"Vamos cadastrar o 1º atleta:")
# Laço while utilizado para registrar um número indefinido de atletas, repetindo o código quantas vezes o usuário quiser.
while cadastro == "s" or cadastro == "sim":

    # Pergunta a idade do atleta limitando a resposta a números inteiros.
    idade = input("Qual a idade do atleta?\n")
    while not idade.isdigit() or int(idade) <= 0 or int(idade) >= 100:
        print("A idade deve ser maior que 0 e menor que 100")
        idade = input("Qual a idade do atleta?\n")
    qntIdades += 1
    somaIdadeGeral += int(idade)

    # Pergunta o sexo do atleta podendo as respostas serem Masculino ou M para homem e Feminino ou F para mulheres.
    sexo = input("Qual o sexo do atleta? [Masculino / M] ou [Feminino / F]\n").lower().strip()[0]
    while not (sexo == "masculino" or sexo == "feminino" or sexo == "m" or sexo == "f"):
        print("Responda com [Masculino / M] ou [Feminino / F]")
        sexo = input("Qual o sexo do atleta? [Masculino / M] ou [Feminino / F]\n").lower()
    
    if sexo == "masculino" or sexo == "m":
        atletasM += 1
    else:
        atletasF += 1

    # Pergunta se o atleta teve febre, sendo as possibilidade de resposta Sim/S ou Não/Nao/N.
    febre = input("O atleta apresentou febre? [Sim / S] ou [Não / N]\n").lower()
    while not (febre == "sim" or febre == "s" or febre == "não" or febre == "nao" or febre == "n"):
        print("Responda com [Sim / S] ou [Não / N]")
        febre = input("O atleta apresentou febre? [Sim / S] ou [Não / N]\n").lower()
    
    if febre == "sim" or febre == "s":    
        temperatura = input("Qual a maior temperatura corporal registrada desde que voltou de Tóquio?(em °C)\n")
        while not temperatura.replace(".","",1).isdigit() or float(temperatura) <= 36 or float(temperatura) > 43:
            print("A temperatura deve ser maior ou igual a 36.0°C e menor que 43.0°C")
            temperatura = input("Qual a maior temperatura corporal registrada desde que voltou de Tóquio?(em °C)\n")
        
        qntSintomas += 1
        qntIdadesComSintomas += 1
        somaIdadeComSintomas += int(idade)
    else:
        sintoma = input("O atleta teve outro sintoma? [Sim / S] ou [Não / N]\n").lower()
        while not (sintoma == "sim" or sintoma == "s" or sintoma == "não" or sintoma == "nao" or sintoma == "n"):
            print("Responda com [Sim / S] ou [Não / N]")
            sintoma = input("O atleta teve outro sintoma? [Sim / S] ou [Não / N]\n").lower()
        
    #Se o atleta não teve febre, pergunta se teve algum sintoma, sendo as possibilidade de resposta Sim/S ou Não/Nao/N.
    if sintoma == "sim" or sintoma == "s":
        qntSintomas += 1
        qntIdadesComSintomas += 1
        somaIdadeComSintomas += int(idade)       
    else:
        qntIdadesSemSintomas += 1
        somaIdadeSemSintomas += int(idade)

    if float(temperatura) > temperaturaMAX: # Trecho de código aprensentado por Luan Barbosa na primeira sessão do MI
        temperaturaMAX = float(temperatura)

    # Caso o atleta tenha apresentado algum sintoma, é comparada a idade para saber se ele é um dos mais novos ou um dos mais velhos.
    if febre == "sim" or febre == "s" or sintoma == "sim" or sintoma == "s":
        if idadeMaisNovo == 0:
            idadeMaisNovo = 100
        if int(idade) > idadeMaisVelho:
            idadeMaisVelho = int(idade)

        if int(idade) < idadeMaisNovo:
            idadeMaisNovo = int(idade)

    # Pergunta se o atleta fez uso do Kit COVID ao retornar ao Brasil.
    kitCovid = input("O atleta tomou o Kit COVID ao retornar ao Brasil? [Sim / S] ou [Não / N]\n").lower()
    while not (kitCovid == "sim" or kitCovid == "s" or kitCovid == "não" or kitCovid == "nao" or kitCovid == "n"):
        print("Responda com [Sim / S] ou [Não / N]")
        kitCovid = input("O atleta tomou o Kit COVID ao retornar ao Brasil? [Sim / S] ou [Não / N]\n").lower()

    # Separa os atletas (M/F) que usaram Kit COVID e tiveram ou não sintomas.
    if kitCovid == "sim" or kitCovid == "s":
        if febre == "sim" or febre == "s" or sintoma == "sim" or sintoma == "s":                  
            if sexo == "masculino" or sexo == "m":
                atletasMKitSintoma +=1
            else:
                atletasFKitSintoma += 1          
        else:        
            if sexo == "masculino" or sexo == "m":
                atletasMKitSemSintoma +=1
            else:
                atletasFKitSemSintoma += 1

    # Pergunta se o atleta recebeu alguma medalha
    medalhas = input("O atleta recebeu alguma medalha? [Sim / S] ou [Não / N]?\n").lower()
    while not (medalhas == "sim" or medalhas == "s" or medalhas == "não" or medalhas == "nao" or medalhas == "n"):
        print("Responda com [Sim / S] ou [Não / N]")
        medalhas = input("O atleta recebeu alguma medalha? [Sim / S] ou [Não / N]?\n").lower()

    #Caso o atleta tenha recebido medalhas, pergunta quantas e quais.
    if medalhas == "s" or medalhas == "sim":
        quantidadeOuro = input("Quantas medalhas de Ouro o atleta recebeu?\n")
        while not quantidadeOuro.isdigit():
            print("Digite um número inteiro maior ou igual a 0")
            quantidadeOuro = input("Quantas medalhas de Ouro o atleta recebeu?\n")

        quantidadePrata = input("Quantas medalhas de Prata o atleta recebeu?\n")
        while not quantidadePrata.isdigit():
            print("Digite um número inteiro maior ou igual a 0")
            quantidadePrata = input("Quantas medalhas de Prata o atleta recebeu?\n")

        quantidadeBronze = input("Quantas medalhas de Bronze o atleta recebeu?\n")
        while not quantidadeBronze.isdigit():
            print("Digite um número inteiro maior ou igual a 0")
            quantidadeBronze = input("Quantas medalhas de Bronze o atleta recebeu?\n")

    # Separa as medalhas que o atleta por gênero (M/F) e por sintomas (S/N)
    if medalhas == "sim" or medalhas == "s":
        if sexo == "masculino" or sexo == "m":
            if febre == "sim" or febre == "s" or sintoma == "sim" or sintoma == "s":
                somaOuroMascComSintoma += int(quantidadeOuro)
                somaPrataMascComSintoma += int(quantidadePrata)
                somaBronzeMascComSintoma += int(quantidadeBronze)
            
            else:
                somaOuroMascSemSintoma += int(quantidadeOuro)
                somaPrataMascSemSintoma += int(quantidadePrata)
                somaBronzeMascSemSintoma += int(quantidadeBronze)
        
        else:
            if febre == "sim" or febre == "s" or sintoma == "sim" or sintoma == "s":
                somaOuroFemComSintoma += int(quantidadeOuro)
                somaPrataFemComSintoma += int(quantidadePrata)
                somaBronzeFemComSintoma += int(quantidadeBronze)
            
            else:
                somaOuroFemSemSintoma += int(quantidadeOuro)
                somaPrataFemSemSintoma += int(quantidadePrata)
                somaBronzeFemSemSintoma += int(quantidadeBronze)

    # Pergunta se deseja cadastrar outro atleta
    cadastro = input("Deseja cadastrar outro atleta?\n").lower()
    while not (cadastro == "sim" or cadastro == "s" or cadastro == "nao" or cadastro == "não" or cadastro == "n"):
        print("Responda com [Sim / S] ou [Não / N]")
        cadastro = input("Deseja cadastrar outro atleta?\n").lower()
    
    if cadastro == "sim" or cadastro == "s":
        print("-------------"*5)
        print(f"Vamos cadastrar o {qntIdades + 1}º atleta:") 
    else:
        print("-------------"*5)
        print("Cadastro finalizado")
        print("-------------"*5)

# Calculos de idade média [Geral/Sintomático/Assintomático]
idadeMediaGeral = somaIdadeGeral / qntIdades
if somaIdadeSemSintomas > 0:
    idadeMediaSemSintomas = somaIdadeSemSintomas / qntIdadesSemSintomas
if somaIdadeComSintomas > 0:
    idadeMediaComSintomas = somaIdadeComSintomas / qntIdadesComSintomas
porcentagemComSintomas = qntIdadesComSintomas / qntIdades * 100

# "1) Quantidade de atletas monitorados"
print(f"\n{qntIdades:.0f} atletas foram monitorados.\n")
# "2) A quantidade e a porcentagem de atletas que apresentaram sintomas;"
print(f"{qntSintomas:.0f} atletas apresentaram sintomas equivaltente a {porcentagemComSintomas:.2f}% dos atletas.\n")
# 3) Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;
print(f"- A média de idade foi de:\n")
print(f"{idadeMediaGeral:.1f} anos entre todos os atletas\n{idadeMediaSemSintomas:.1f} anos entre os atletas que não apresentaram sintomas\n{idadeMediaComSintomas:.1f} anos entre os atletas sintomáticos\n")
# 4) A temperatura corporal mais alta relatada;
print(f"A temperatura corporal mais alta relatada foi de {temperaturaMAX:.1f}°C.\n")
# 5) Dentre os que apresentaram sintomas, a idade do atleta mais novo e do atleta mais velho;
print(f"Dentre os atletas que apresentaram sintomas, o atleta mais novo possui {idadeMaisNovo:.0f} anos de idade e o mais velho possui {idadeMaisVelho:.0f} anos de idade.\n")
# 6) Um recorte por gênero dos atletas que tomaram o “kit COVID”, indicando ainda, dentre estes, a quantidade de homens e mulheres que tiveram ou não sintomas;
print(f"{atletasMKitSemSintoma + atletasMKitSintoma:.0f} atletas homens e {atletasFKitSemSintoma + atletasFKitSintoma:.0f} atletas mulheres utilizaram o Kit COVID.\n")
print(f"Dentre os atletas homens que tomaram o Kit COVID {atletasMKitSintoma:.0f} atletas apresentaram sintomas e {atletasMKitSemSintoma:.0f} atletas não apresentaram sintomas.\n")
print(f"Dentre as atletas mulheres que tomaram o Kit COVID {atletasFKitSintoma:.0f} atletas apresentaram sintomas e {atletasFKitSemSintoma:.0f} atletas não apresentaram sintomas.\n")
# 7) Um recorte por gênero (M/F) e por sintomas (S/N) dos atletas que trouxeram medalhas para casa, especificando a quantidade de medalhas de ouro, prata e bronze.
print("A quantidade de medalhas recebida foi de:\n- Dentre os atletas que tiveram sintomas")
print(f"[Sexo Masculino]\nOuro: {somaOuroMascComSintoma:.0f}\nPrata: {somaPrataMascComSintoma:.0f}\nBronze: {somaBronzeMascComSintoma:.0f}\n")
print(f"[Sexo Feminino]\nOuro: {somaOuroFemComSintoma:.0f}\nPrata: {somaPrataFemComSintoma:.0f}\nBronze: {somaBronzeFemComSintoma:.0f}\n")
print(f"- Dentre os atletas que não tiveram sintomas")
print(f"[Sexo Masculino]\nOuro: {somaOuroMascSemSintoma:.0f}\nPrata: {somaPrataMascSemSintoma:.0f}\nBronze: {somaBronzeMascSemSintoma:.0f}\n")
print(f"[Sexo Feminino]\nOuro: {somaOuroFemSemSintoma:.0f}\nPrata: {somaPrataFemSemSintoma:.0f}\nBronze: {somaBronzeFemSemSintoma:.0f}\n")
print("Obrigado por utilizar nosso programa :D")
input("Aperte qualquer tecla para finalizar.")