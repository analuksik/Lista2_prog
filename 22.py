soma = 0
q = 0
while True:
  try:
    temp = float(input(f'Digite a temperatura em graus Celsius (°C): '))
    if (temp < -15) or (temp < 5):
      soma += temp
      q += 1
      
    else:
      break

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

if q > 0:    
  media = soma / q
  print(f'A média das temperaturas é de: {media}°C')
else:
  print('Nenhum valor válido foi inserido. ')

    
