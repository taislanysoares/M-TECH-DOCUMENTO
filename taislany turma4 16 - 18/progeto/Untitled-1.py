#crie um programa que peça uma senha ao usuario

senha_correta ="12345"
tentativas = 3

while tentativas > 0:
    senha= input("digite sua senha :") 
    
    if senha == senha_correta:
        print("acesso permitido!")
        break
   
    else: 
     tentativas -=1
     print(f"senha_incrreta! voce tem: {tentativas} tentativas ")
   
    if tentativas == 0:
     print("acesso bloqueao!")   
 
