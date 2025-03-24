try:
  soma = 0
  q = 0
  n = int(input("Digite o valor de n: "))
  if n < 0:
    print("ERRO: O VALOR DE n DEVE SER POSITIVO")
    exit()
  for i in range(n,n+50):
    soma += 1
    q += 1
    print(f"O {q}° número subsequente de {n} é: {soma}")

except Exception as ERRO_EXCECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")


