def sacar(valor):
    saldo = 500
    if valor >= saldo:
        print("Saldo insuficiente.")
        print("Tente um valor menor.")

    print("Saque realizado com sucesso.")

def depositar(valor):
    saldo = 500
    saldo += valor
    if valor <= 0:
        print("Valor inválido para depósito.")
    else:
        valor > 0
        print("Depósito realizado")
        print("Novo saldo:", saldo)
