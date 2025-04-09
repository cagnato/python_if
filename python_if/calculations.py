# print("Bem vindo à calculadora legal do Davi!!!")

# operacao = (input("insira a operação que deseja: 1. Soma, 2. Subtração, 3. Divisão, 4. Multiplicação "))

# a = int(input("Insira o primeiro número: "))
# b = int(input("Insira o segundo número: "))



# if operacao == 1:
#     soma = a + b
#     print(soma)
# elif operacao == 2:
#     subtracao = a - b
#     print(subtracao)
# elif operacao == 3:
#     divisao = a / b
#     print(divisao)
# elif operacao == 4:
#     multiplicacao = a * b
#     print(multiplicacao)




print("Bem-vindo à calculadora legal do Davi!!!")

operacao = float(input("Insira a operação que deseja: 1. Soma, 2. Subtração, 3. Divisão, 4. Multiplicação "))

if operacao <= 0 or operacao >= 5:
    print("Operação inválida!")
else:
    a = float(input("Insira o primeiro número: "))
    b = float(input("Insira o segundo número: "))

    if operacao == 1:
        soma = a + b
        print(f"Resultado: {soma:.2f}")
    elif operacao == 2:
        subtracao = a - b
        print(f"Resultado: {subtracao:.2f}")
    elif operacao == 3:
        divisao = a / b
        print(f"Resultado: {divisao:.2f}")
    elif operacao == 4:
        multiplicacao = a * b
        print(f"Resultado: {multiplicacao:.2f}")



# match operacao:
#     case 1:
#         print("Resultado:" + str(a + b))
#     case 2:
#         print("Resultado: " + (a - b))