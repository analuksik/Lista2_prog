try:
  print('Os múltiplos de 7 ou de 13 no intervalo [1000, 1500] são: ')

  for i in range(1000, 1501):
    if i % 7 == 0 or i % 13 == 0:
      print(f'{i}')
except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXECAO}')      
