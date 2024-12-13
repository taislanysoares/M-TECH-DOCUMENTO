nota1 = float(input("digite um numero:"))
nota2 = float(input("digite um numero:"))
nota3 = float(input("digite um numero:"))

media  = (nota1+nota2+nota3) /3

if media <5:
     print (f"reprovado")
elif  5 <= media <7:
     print(f"recuperação")
else:
     print(f" aprovado")
        
 