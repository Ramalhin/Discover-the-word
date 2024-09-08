import os

palavraSecreta = "adivinhe"
letrasAcertadas = ""
tentativas = 0
while True:

    tentativas += 1
    letraDigitada = input("digite uma letra")
    if len(letraDigitada) > 1:
        print("Você digitou mais de uma letra, tente novamente")
        continue

    if letraDigitada in palavraSecreta:
        letrasAcertadas += letraDigitada

    palavraFormada = ""
    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasAcertadas:
            palavraFormada += letraSecreta

        else:
            palavraFormada += "*"

    print(palavraFormada)

    if palavraFormada == palavraSecreta:
        os.system('cls')
        print("Parabéns você acertou a palavra secreta")
        print(f"a palavra era: {palavraSecreta}")
        print(f"tentativas = {tentativas}")
        palavraSecreta = "adivinhe"
        letrasAcertadas = ""
        tentativas = 0


