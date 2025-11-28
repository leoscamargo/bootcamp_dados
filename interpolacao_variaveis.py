nome = "Leonardo"
idade = 26
profissao = "Analista de TI"
linguagem = "Python"

print("Olá, meu nome é %s, tenho %d anos, sou %s e trabalho com %s." % (nome, idade, profissao, linguagem)) ##old style

print("Olá, meu nome é {}, tenho {} anos, sou {} e trabalho com {}.".format(nome, idade, profissao, linguagem))

print("Olá, meu nome é {0}, tenho {1} anos, sou {2} e trabalho com {3}.".format(nome, idade, profissao, linguagem))

print("Olá, meu nome é {nome}, tenho {idade} anos, sou {profissao} e trabalho com {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print(f"Olá, meu nome é {nome}, tenho {idade} anos, sou {profissao} e trabalho com {linguagem}.") ##f-string

PI = 3.14159
print("O valor de PI é aproximadamente %.2f." % PI) ##old style
print(f"O valor de PI é aproximadamente {PI:2.2f}.") ##f-string