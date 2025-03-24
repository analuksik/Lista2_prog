try:
  soma = 0
  qtd = 0
  x = int(input("Digite o valor de x: "))
  if x < 1:
      print("ERRO DADOS DE ENTRADA: x DEVE SER >= 1")
      exit()
  for i in range(6, 6 * x, 6):
    soma += i
    qtd += 1
    media = soma // qtd
    print(f"A média dos múltiplos de 6 no intervalo [6, 6 * {x}] é: {media}.")
except Exception as ERRO_EXCECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")
