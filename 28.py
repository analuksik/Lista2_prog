import math

try:

  n = int(input('Digite um valor para n: '))

  if n >= 1:
      soma, mult = 0, 1

      for i in range(1, n+1, 2):
          soma += math.pi + (math.pi / i)

      for i in range(1, n+1, 2):
          mult *= i / math.pi

      print(f"Soma (S) = {soma}")
      print(f"Multiplicação (M) = {mult}")
  else:
      print("Por favor, insira um valor inteiro positivo para n.")
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
