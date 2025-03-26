
cont = 0
soma = 0
n = 10
while True:

  try:
    cont += 1
    n = int(input(f"Digite o {cont}º valor para n: "))

    if n == 0:
      break

    if n >= 10 and n <= 90 and n % 5 == 2:
      soma += n  

  except Exception as ERRO_EXCECAO:
    print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")
    
print(f"A soma dos números lidos é: {soma}")
