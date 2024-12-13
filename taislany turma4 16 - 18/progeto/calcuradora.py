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
operação = input("digite o número da operação desejada:") 
#realiza a operação escolhida
if operação =='1':
    resultado = num1 +num2
    print(f"\nO resultado de {num1} + {num2} é:
   {resultado}")
elif operação =='2':
    resultado = num1 - num2
    print(f"\nO resultado de {num1} - {num2} é:
{resultado}")
else: 
    print("\nOperação inválida.por favor,escolha uma operação entre 1 e 4.")