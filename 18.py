contador, soma = 0, 0
while contador < 100:
  try:
    n = int(input(f'Digite o {contador + 1}° número que seja ímpar e múltiplo de 7: '))
    if (n % 2 == 0) or (n % 7 != 0):
      print('O número deve ser ímpar e múltiplo de 7!')
    else:
      soma += n
      contador += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')    
media = soma / 5    
print(f"A média dos números digitados é: {media}")
