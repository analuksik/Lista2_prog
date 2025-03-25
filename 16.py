num = 0
maiorNum_par, maiorNum_impar = None, None
menorNum_par, menorNum_impar= None, None
while num < 300:
  try:
    n = int(input("Digite o valor de n: "))
    if n % 2 == 0:
      if maiorNum_par is None or n > maiorNum_par:
        maiorNum_par = n
      if menorNum_par is None or n < menorNum_par:
        menorNum_par = n
    else: 
      if maiorNum_impar is None or n > maiorNum_impar:
        maiorNum_impar = n
      if menorNum_impar is None or n < menorNum_impar:
        menorNum_impar = n
    num += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

print(f'O maior número par é: {maiorNum_par}')  
print(f'O menor número par é: {menorNum_par}')
print(f'O maior número ímpar é: {maiorNum_impar}')
print(f'O menor número ímpar é: {menorNum_impar}')
