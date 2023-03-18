tamanho = str(input("Qual o tamanho do(s) ovo(s) de pascoa que você deseja? (Pequeno, Médio ou Grande)"))
sabor = str(input("Qual o sabor do(s) ovo(s) de pascoa que você deseja? (Chocolate Preto, Chocolate ao Leite ou Chocolate Branco)"))
# recheio = str(input("Qual o recheio que você deseja? (Chocolate Branco ou Chocolate Preto)"))
# recheio2 = str(input("Você deseja outro recheio se sim qual? (Se não desejar digite N"))
# adicionais = str(input("Qual adicional você deseja acrescentar? (KitKat ou MM's)"))
# presente = str(input("O seu ovo(s) será para Presente ou Entrega?"))
# quantidade = int(input("Por fim, quantos ovos você irá querer?"))
# pagamento = str(input("Como você deseja realizar o pagamento? (Cartão, Dinheiro ou Pix)"))

valor = 0
valor2 = 0
# valor3 = 0
# valor4 = 0
# valor5 = 0
# valor6 = 0
# valor7 = 0
valorfinal = float

valor

if tamanho == "Pequeno":
    valorfinal = valor + 7.8
elif tamanho == "Médio":
    valorfinal = valor + 12.9
elif tamanho == "Grande":
    valorfinal = valor + 23.95

if sabor == "Chocolate Preto":
    valorfinal = valor + 9.67
elif sabor == "Chocolate ao Leite":
    valorfinal = valor + 9.32
elif sabor == "Chocolate Branco":
    valorfinal = valor + 4.50

# if recheio == "Chocolate Branco":
#     valorfinal = valor3 + 2.25
# elif recheio == "Chocolate Preto":
#     valorfinal = valor3 + 4.83

# if recheio2 == "Chocolate Branco":
#     valorfinal = valor4 + 2.25/2
# elif recheio2 == "Chocolate Preto":
#     valorfinal = valor4 + 4.83/2
# elif recheio2 == "N":
#     valorfinal = valor4 + 0

# if adicionais == "KitKat":
#     valorfinal = valor5 + 4.67
# elif adicionais == "MM's":
#     valorfinal = valor5 + 5.43

# if presente == "Presente":
#     valorfinal = valor6 + 2.50
# elif adicionais == "Entrega":
#     valorfinal = valor6 + 5.00

# valorfinal = valor * quantidade

# if pagamento == "Cartão":
#     valorfinal = valor7 + 3.30
# elif pagamento == "Dinheiro":
#     valorfinal = valor7 * 0.1
# elif pagamento == "Pix":
#     valorfinal = valor7 * 0.1

valorfinal = valor + valor2
#  + valor3 + valor4 + valor5 + valor6 +valor7

print ("O valor final de seu ovo(s) é de ", valorfinal)
