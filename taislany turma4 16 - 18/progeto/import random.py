import random 
numero_secreto = random.randit  (1, 100)
tentativas = 0 
while tentativas < 5:
    numero = input (" digite um numero:")
    if num == numero_secreto:
        print("voce acertou")
        break 
else:
    tentativas =+1
    print("senha incorreta.tentativas restantes:")
if tentativas == 5:
    print("numero maximo de tentativas atingido.acesso bloqueado:")
