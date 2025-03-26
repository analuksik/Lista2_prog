neg, pos = 0, 0
total_posi, total_neg = 0, 0
mediaPosi, mediaNeg= 0, 0

while True:
  try:
    n = int(input("Digite um valor para n, ou digite 0 para sair do programa: "))

    if n == 0:
      print('FIM DO PROGRAMA! ')
      break
    elif n > 0:
      pos += n
      total_posi += 1
    else:
      neg += n
      total_neg += 1
  
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

if total_posi > 0:  
  mediaPosi = (pos / total_posi) 
  print(f'A média dos números positivos lidos é: {mediaPosi}')    
else:
  print('Nenhum número positivo foi digitado.')

if total_neg > 0:
  mediaNeg = (neg / total_neg)
  print(f'A média dos números negativos digitados é: {mediaNeg}')
else:
  print('Nenhum número negativo foi digitado')
