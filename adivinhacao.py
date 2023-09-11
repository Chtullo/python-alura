print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("você digitou ", chute_str)

chute = int(chute_str)

acertou     = numero_secreto == chute

chute_maior = chute > numero_secreto

chute_menor = chute < numero_secreto

if acertou:
    print("você acertou!")
else:
    if chute_maior:
        print("Você errou! O seu chute foi maior do que o numero secreto.")
    elif chute_menor:
        print("Você errou! O seu chute foi menor do que o numero secreto.")

print("Fim do jogo.")
