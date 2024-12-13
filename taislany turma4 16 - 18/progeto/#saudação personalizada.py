#saudação personalizada 

nome=input("qual e seu nome?")
hora=int(input("que horas são agora(apenas a hora)?"))
if 6 <=hora < 12:
 print(f"bom dia,{nome}!")
elif 12 <=hora<18:
  print(f"boa tarde,{nome}!")
else: 
  print(f"boa noite,{nome}!")
         
