peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso/(altura*altura)

if imc < 18.5:
    print("Você é magro")
elif imc > 18.5 and imc < 24.9:
    print("Você está no peso ideal")
elif imc > 25 and imc < 29.9:
    print("Você possui sobrepeso")
elif imc > 30 and imc < 34.9:
    print("Você possui Obesidade grau 1")
elif imc > 35 and imc < 39.9:
    print("Você possui Obesidade grau 2")
else:
    print("Você possui Obesidade grau 3")

print ("Seu IMC é de: ", imc)
