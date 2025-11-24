maior_idade = 18
idade = int(input("Digite sua idade: "))
if idade >= maior_idade:
    print("Você é maior de idade, pode tirar a CNH.")
else:
    print("Você é menor de idade, não pode tirar a CNH.")


saldo = 2000
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    saldo -= saque
    print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
else:
    print("Saldo insuficiente para realizar o saque.")


opcao = int(input("Informe uma opção: 1 - Depositar, 2 - Sacar, 3 - Sair: "))
if opcao == 1:
    valor = float(input("Digite o valor do depósito: "))
    saldo += valor
    print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")
elif opcao == 2:
    valor = float(input("Digite o valor do saque: "))
    if saldo >= valor:
        saldo -= valor
        print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente para realizar o saque.")
elif opcao == 3:
    print("Encerrando sua sessão...")
else:
    print("Opção inválida.")

