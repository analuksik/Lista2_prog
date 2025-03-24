q = 1
somaPosi, somaNeg = 0, 0
porcPosi, porcNeg, total = 0, 0, 0

while True:
  try:

    n = int(input(f"Digite o {q}° valor de n: "))
    q += 1
    if n < 0:
      somaNeg += 1
    elif n > 0:
      somaPosi += 1
    elif n == 0:
      break

    total += 1   

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    
if total > 0:
  porcPosi = (somaPosi / total) * 100
  porcNeg = (somaNeg / total) * 100
  print(f'De {total} números lidos, {porcPosi}% foram positivos')
  print(f'E {porcNeg}% foram negativos')

else:
  print("ERRO: DIVISÃO POR 0")
