"""
Bem vindo ao código do meu Jogo da Forca!

Neste jogo o jogador tem que conseguir adivinhar a palavra, escolhida aleatoriamente pelo computador, inserindo uma letra de cada vez ou uma palavra.
Não são permitidos números nem caracteres complexos (ex: ~, `, ´, *, +, \, ç, ñ, etc.)
Por cada tentativa falhada o boneco da forca vai sendo desenhado.
Se o boneco ficar completo, perdes.

Boa sorte!

"""
## Este import permite usar comandos da consola do Windowss
import os
import random

## O script usa o comando da consola do Windows que limpa o texto da consola quando esta função é chamada
def limpa_ecran():
    os.system("cls")
    

def define_palavra(palavras):

    global ESCOLHA_PALAVRA

    ESCOLHA_PALAVRA = random.randrange(len(palavras))
    palavra = palavras[ESCOLHA_PALAVRA]
    palavra_do_jogo = [letra for letra in palavra]
    
    return palavra_do_jogo


def esconde_palavra(comprimento):

    for letra in range(len(palavra_misterio)):
        comprimento.append("_")
        
    return comprimento


def verifica_numerico(i_utilizador):
    
    for char in i_utilizador:
        if char.isdigit():
            return True
        
    return False


def verifica_char_complexo(i_utilizador):
    
    for char in i_utilizador:
        if ord(char) not in range(65, 91) and ord(char) not in range(97, 123):
            return True
        
    return False


def processa_palavra(i_utilizador):

    global TIPO_TENTATIVA, PALAVRA_ESCONDIDA
    
    if verifica_numerico(i_utilizador):
        print("\nNão pode ser valores numéricos!")
        ## Com esta linha, o script usa o comando da consola do Windows que pausa a execução.
        os.system("pause")


    elif verifica_char_complexo(i_utilizador):
        print("\nNão pode ser caracteres complexos!")
        os.system("pause")
        

    elif len(i_utilizador) > 1 and len(i_utilizador) < len(PALAVRA_ESCONDIDA):
        print("\nTentativa demasiado curta!")
        os.system("pause")
        

    elif len(i_utilizador) > len(PALAVRA_ESCONDIDA):
        print("\nTentativa demasiado comprida!")
        os.system("pause")

        
    elif len(i_utilizador) == 1:
        
        TIPO_TENTATIVA = "letra"
    
        if i_utilizador.lower() in palavra_misterio or i_utilizador.upper() in palavra_misterio:
            
            for letra in range(len(palavra_misterio)):
                
                if  i_utilizador == palavra_misterio[letra]:
                    PALAVRA_ESCONDIDA[letra] = i_utilizador
                    
                if i_utilizador.lower() == palavra_misterio[letra]:
                    PALAVRA_ESCONDIDA[letra] = i_utilizador.lower()
                    
                if i_utilizador.upper() == palavra_misterio[letra]:
                    PALAVRA_ESCONDIDA[letra] = i_utilizador.upper()

        else:
            classifica_falha(tentativas)
            

    elif len(i_utilizador) == len(palavra_misterio):

        TIPO_TENTATIVA = "palavra"

        p_escondida_ant = []
        
        p_escondida_ant += PALAVRA_ESCONDIDA

        for letra in range(len(palavra_misterio)):
                    
            if i_utilizador.capitalize()[letra] == palavra_misterio[letra]:
                PALAVRA_ESCONDIDA[letra] = i_utilizador.capitalize()[letra]
                
            else:
                PALAVRA_ESCONDIDA = p_escondida_ant
                classifica_falha(tentativas)
                return


def classifica_falha(tentativas):

    global JOGADA, BONECO

    if i_utilizador.lower() not in tentativas and i_utilizador.upper() not in tentativas:
        
        if TIPO_TENTATIVA == "letra":
            print("\nA palavra não tem essa letra!")
            os.system("pause")
            
        else:
            print("\nPalavra errada!")
            os.system("pause")
            
        if dificuldade == "dificil" or dificuldade == "d" or dificuldade == "medio" or dificuldade == "m":
            tentativas.append(i_utilizador)
            BONECO += ''.join(forca_dificil[JOGADA])
            JOGADA += 1 
            
        elif dificuldade == "facil" or dificuldade == "f":
            tentativas.append(i_utilizador)
            BONECO += ''.join(forca_facil[JOGADA])
            JOGADA += 1
            
    else:
        print("\nEssa tentativa já foi feita!")
        os.system("pause")
            

palavras = ["Mundo", "Idade", "Soma", "Media", "Notas", "Ciclo", "Tabuada", "Primo", "Dados", "Euromilhoes"]
dicas = ["Globo terrestre.", "Tempo transcorrido desde o nascimento ou desde o princípio.", "Operação em que se juntam duas ou mais parcelas para obter um número total.",
          "Quociente da divisão de uma soma pelo número das parcelas.", "Classificação que avalia a qualidade de um trabalho, exercício, exame ou desempenho.",
          "Série de fenómenos que se sucedem numa ordem determinada.", "Folheto ou tabela que ensina as primeiras noções dos números.", "Que só é divisível por si próprio e por 1." ,
          "Pequenos cubos que tem em cada face um determinado número de pontos.", "Jogo de azar que funciona como uma espécie de lotaria de números."]

while True:
    
    ESCOLHA_PALAVRA = 0
    comprimento = []
    BONECO = "\n\nForca:\n _ \n  | "
    forca_dificil = ["\n  O", "\n /", "|", "\ ", "\n /", " \ \n"]
    forca_facil = ["\n  O", "\n /", "|", "\ ", "\n´", "/", " \\", "`", "\n´", "   `"]
    JOGADA = 0
    TIPO_TENTATIVA = ""
    tentativas = []
    palavra_misterio = define_palavra(palavras)
    p_mist = ''.join(palavra_misterio)
    PALAVRA_ESCONDIDA = esconde_palavra(comprimento)
    
    print("{:s}".format("\u0332".join("\nJogo Da Forca ")))     ## \u0332 = sublinhado   e   \u0333 = sublinhado duplo
    dificuldade = input("\nQueres um jogo fácil (f), médio (m) ou difícil (d)?: ").casefold()
    
    if dificuldade == "dificil" or dificuldade == "d" or dificuldade == "medio" or dificuldade == "m":
        duracao_jogo = len(forca_dificil)
            
    elif dificuldade == "facil" or dificuldade == "f":
        duracao_jogo = len(forca_facil)

    else:
        dificuldade = "medio"
        duracao_jogo = len(forca_dificil)
        print(f"\nComando inválido. A dificuldade ficou definida como '{dificuldade}'.")
        os.system("pause")

    limpa_ecran()   

    while "_" in PALAVRA_ESCONDIDA and JOGADA < duracao_jogo:

        print("{:s}".format("\u0332".join("\nJogo Da Forca ")))
        print(f"{BONECO} \n\n\n")
        p_esc = ' '.join(PALAVRA_ESCONDIDA)
        print(p_esc)
            
        if dificuldade == "medio" or dificuldade == "m" or dificuldade == "facil" or dificuldade == "f":
            print(f"\n\nDica: {dicas[ESCOLHA_PALAVRA]}")
            
        else:
            print("\n\n")
                   
        p_tent = ' '.join(tentativas)
        print(f"Tentativas erradas: {p_tent}")

        i_utilizador = input(f"\nEscreve uma letra ou uma palavra de {len(palavra_misterio)} letras: ")

        processa_palavra(i_utilizador)
        
        limpa_ecran()
        

    if JOGADA == duracao_jogo:
        print("{:s}".format("\u0332".join("\nJogo Da Forca ")))
        print(BONECO)
        print(f"\nPerdeste.\nA palavra era: {p_mist}.\n\n")


    else:
        print("{:s}".format("\u0332".join("\nJogo Da Forca ")))
        p_esc = ' '.join(PALAVRA_ESCONDIDA)
        print(f"\n\n {p_esc}")
        print("\nGanhaste!\n\n")
        

    escolha = input("Queres jogar de novo? (S/N) ").casefold()

    if escolha == "não" or escolha == "nao" or escolha == "ñ" or escolha == "n":
        print("\nEspero que tenhas gostado! Adeus!\n")
        os.system("pause")
        break
    
    else:
        limpa_ecran()
