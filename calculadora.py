# Calculadora

print("Calculadora")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("+  Soma")
print("-  Subtração")
print("*  Multiplicação")
print("/  Divisão")
print("** Potencia")

operacao = input("Escolha a operação: ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado é: {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado é: {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado é: {resultado}")

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Não existe divisão por zero")

elif operacao == "**":
    if num2 != 0:
        resultado = num1 ** num2
        print(f"Resultado: {resultado}")

else:
    print("Operação inválida!")
