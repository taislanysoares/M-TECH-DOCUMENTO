#escreva um progroma que solicite tres notas de um aluno 
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
 
media = (nota1+nota2+nota3)

if media >= 7:
    print("f aluna aprovada {media:.2f}")
elif