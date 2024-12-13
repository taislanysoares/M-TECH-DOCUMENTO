#senha123
senha_sistema = "minha_senha123"
tentativas = 0
while tentativas < 3:
    senha_usuario = input ("digite a  senha:")
    if senha_usuario == senha_sistema:
     print("acesso concedido!")
     break
else:
   tentativas +=1
   print(f"senha incorreta. tentativas restantes: {3 - tentativas}")
   if tentativas == 3:
      print("numero maximo de tentativas atingido.acesso bloqueado.")