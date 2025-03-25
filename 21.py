import math

soma, total = 0, 0

while True:
  try:
    n = float(input("Digite um valor para n: "))
    if n > (10 * math.pi) and n < (100 * math.pi):
      soma += n
      total += 1
    else:
      break

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')  

if total > 0:
  media = soma / total
  print(f"A média dos números digitados que estão no intervalo [10 * π³, 100 * π] é: {media}.")

else: 
  print('Nenhum número válido foi inserido! ')
