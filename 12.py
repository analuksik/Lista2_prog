try:
  soma = 0
  q = 0
  while True:
    temp = float(input(f'Digite a temperatura em graus Celsius (°C): '))
    if temp < 28:
      break
    else:
      soma += temp
      q += 1
  media = soma / q
  print(f'A média das temperaturas é de: {media}°C')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')


    
