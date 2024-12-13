#calcuradora basica 
#solicita dois numeros ao usuario
num1 = float(input("digite o primeiro numero:"))
num2 = float(input("digite o segundo numero:"))
#exibe as opçoes de operaçoes
print("\nEscolha a operaçoes:")
print("1 - Adição")
print("2 - subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#solicita a escolha da operação
operacao = input("digite o número da operação desejada:") 

#realiza a operação escolhida
if operacao =='1':
    resultado = num1 + num2
    print(f"\nO resultado de {num1} + {num2} é: {resultado}")

elif operacao =='2':
    resultado = num1 - num2
    print(f"\nO resultado de {num1} - {num2} é: {resultado}")

elif operacao =='3':
    resultado = num1 * num2
    print(f"\nO resultado de {num1} * { num2} é: {resultado}")

elif operacao =='4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nO resultado de {num1} / {num2} é: {resultado}")

else: 
    print("\nOperação inválida.por favor,escolha uma operação entre 1 e 4.")