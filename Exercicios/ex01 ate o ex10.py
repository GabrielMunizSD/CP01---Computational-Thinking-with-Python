
#Exercicio 1

numero = int(input("Digite um número inteiro: \n"))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número é zero")



#Exercicio 2

numero = int(input("Digite um número inteiro: \n"))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar")



#Exercicio 3

idade = int(input("Digite sua idade: \n"))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


#Exercicio 4

    nota = float(input("Digite a nota do aluno (0 a 10): \n"))

if nota >= 6:
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")



#Exercicio 5

numero1 = int(input("Digite o primeiro numero inteiro: \n"))
numero2 = int(input("Digite o segundo numero inteiro: \n"))

if numero1 > numero2:
    print("O primeiro numero é maior do que o segundo numero")
elif numero1 < numero2:
    print("O segundo numero é maior do que o primeiro numero")
else:
    print("Os dois numeros sao iguais")



#Exercicio 6

valor_produto = float(input("Digite o valor do produto: \n"))

if valor_produto > 100:
    valor_final = valor_produto * 0.9
    print(f"O preço final do produto com desconto ficou R${valor_final}, totalizando um desconto de R${valor_produto * 0.1}")
else:
    print(f"O preço do produto eh R${valor_produto}")



#Exercicio 7

nome_de_usuario = input("Digite o nome de usuario: \n")
senha = input("Digite a senha: \n")

if nome_de_usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")



#Exercicio 8

    numero = int(input("Digite um número inteiro: \n"))

if numero % 2 == 0:
    print("Par")
elif numero % 5 == 0:
    print("Multiplo de 5")
else:
    print("Outro numero")



#Exercicio 9

temperatura = float(input("Digite a temperatura em graus Celsius: \n"))

if temperatura < 0:
    print("Congelante")
elif temperatura <= 30:
    print("Agradável")
else:
    print("Quente")



#Exercicio 10

numero1 = int(input("Digite o primeiro numero inteiro: \n"))
numero2 = int(input("Digite o segundo numero inteiro: \n"))
operacao = input("Digite a operacao (+, -, *, /): \n")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operacao invalida"

print(f"Resultado: {resultado}")




