#escreva um programa que solicita tres notas de aluno
nota1 = float(input("Digite um numero: " ))
nota2 = float(input("digite um numero: " ))
nota3 = float(input("digite um numero:" ))
  
media = ((nota1+nota2+nota3)/3) 

if media <5:
    print(f'reprovado. {media:.2f}')
elif 5 <= media <7:
     print(f'recuperação. {media:.2f}')
else:
     print(f'aprovado. {media:.2f}')