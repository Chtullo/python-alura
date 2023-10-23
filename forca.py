import random


def jogar():
    imprime_boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Você ganhou!")


def imprime_mensagem_perdedor():
    print("Que pena, você perdeu.")


def imprime_boas_vindas():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


if __name__ == "__main__":
    jogar()
