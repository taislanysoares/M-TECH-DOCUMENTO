#tendo como dado de entreda a altura (h) de uma pessoa,construa um algoritimo que calcule seu
#peso ideal,ultilizando as seguintes formulas:

altura = float (input ( "digite sua altura "))
peso_ideal_h = ( 72.7 * altura) - 58
peso_ideal_m = ( 61.* altura) - 44.7
print(f" o peso ideal para sua altura e.\n {peso_ideal_h:.2f} kg para homens )\n"
      f"{peso_ideal_m:.2f}  kg para mulheres")