saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= saque and saque <= limite
# False

saldo >= saque or saque <= limite
# True

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# True

exp = 2 (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# True

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp3 = conta_especial_com_saldo_suficiente or conta_normal_com_saldo_suficiente
print(exp3)

not 1000 > 500
# False

contatos_emergencia = []
not contatos_emergencia
# True

not "saque 1500"
# False
