# numero = int(input("Digite um número: "))
# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

idade = int(input("Digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else: 
    print("Valor inválido!")
