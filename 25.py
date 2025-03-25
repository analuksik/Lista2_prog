import math

for i in range(0, 500):

  try:

    idade = int(input('Digite a idade do paciente: '))

    if idade < 1:
      print('A idade deve ser maior do que zero. ')
      continue

    massa = float(input('Digite a massa do paciente (kg): '))
    diab = str(input('O paciente é diabético? (S/N) '))

    if diab == 'S':
      taxa = (math.sqrt(massa)) / (0.93 * idade)

    elif diab == 'N':
      taxa = (math.sqrt(0.98 * massa)) / (1.08 * idade)
    else:
      print('Resposta inválida!')
      print('Digite "S" para sim ou "N" para não')

    print(f'A taxa de glicose do paciente é de: {taxa:.2f}')

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')  
