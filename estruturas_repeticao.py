# Estrutura de repetição - for
texto = input("Informe um texto: ")
vogais = "AEIOU"
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")
else:
    print()

#função range
list(range(4))
for numero in range(4):
    print(numero, end=" ")
else:
    print()


for numero in range(0, 51, 5):
    print(numero, end=" ")
else:
    print()

# Estrutura de repetição - while
opcao = -1
while opcao != 0:
    opcao = int(input("[1] - Continuar\n[0] - Sair\nEscolha uma opção: "))
    if opcao == 1:
        print("Você escolheu continuar.")
    elif opcao == 0:
        print("Encerrando o programa...")
    else:
        print("Opção inválida, tente novamente.")

for numero in range(100):
    if numero %2 == 0:
        print(numero, end=" ")