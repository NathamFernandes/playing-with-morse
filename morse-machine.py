import string

## Variable declaration

alfabeto = list(string.ascii_uppercase)
lista_morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
palavra_cripto = []
palavra_uncripto = []

## Functions to encrypt or decrypt

def criptoPalavraMorse(palavra_input):
    for n in palavra_input:
        index_normal = alfabeto.index(n)
        letra_morse = lista_morse[index_normal]
        palavra_cripto.append(letra_morse)

def uncriptoPalavraMorse(palavra_input):
    convertido_morse = palavra_input.split()
    for n in convertido_morse:
        index_morse = lista_morse.index(n)
        letra_normal = alfabeto[index_morse]
        palavra_uncripto.append(letra_normal)
        
## Loop where the program runs

while True:
    escolha = int(input("Escolha a opção \n \n1 - Criptografar em morse \n2 - Descriptografar código morse \n \nResposta: "))
    if escolha == 1:
        palavra_cripto = []
        palavra_input = str(input("Insira a palavra a ser criptografada em morse (apenas letras maiúsculas): "))
        criptoPalavraMorse(palavra_input)
        print(" ".join(map(str, palavra_cripto)))

    elif escolha == 2:
        palavra_uncripto = []
        palavra_input = str(input("Insira o código morse a ser descriptografado: "))
        uncriptoPalavraMorse(palavra_input)
        print("".join(map(str, palavra_uncripto)))
    
    else:
        print("Opção inválida, programa encerrado.")
        break
