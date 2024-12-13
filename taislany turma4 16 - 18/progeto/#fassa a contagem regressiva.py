#fassa a contagem regressiva
tempo_inicial = int(input("digite um numero para iniciar a contagem "))

while tempo_inicial >=0:
    print(tempo_inicial)
    comando = input("digite 'interromper' para parar:").lower()
    if comando == "interromper":
        print("contagem regressiva interropida.")
        break           
    tempo_inicial -=1
if tempo_inicial <0:
  print("contagem regressiva concluida!")