#estrutura de repetição. o programa verifica se a versão maiúscula da letra está na variável VOGAIS
#loop structure. The program checks if the uppercase version of the letter is in the VOGAIS variable.

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()