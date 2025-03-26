contador = 0
mediaFund, mediaMed, mediaSup = 0, 0, 0
totalFund, totalMed, totalSup = 0, 0, 0
salFund, salMed, salSup = 0, 0, 0

while contador < 5:

  try:

    print('Qual seu nível de escolaridade: ')
    escolaridade = str(input('Fundamental, Médio, ou Superior? ')).upper()
    print()
    salario = float(input("Qual é o seu salário? "))
    print()

    if escolaridade == 'FUNDAMENTAL':
      salFund += salario
      totalFund += 1
    
    elif escolaridade in ('MEDIO', 'MÉDIO'):
      salMed += salario
      totalMed += 1

    elif escolaridade == 'SUPERIOR':
      salSup += salario
      totalSup += 1
    
    contador +=1 

  except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

if totalFund > 0:  
  mediaFund = (salFund / totalFund)
  print(f'A média salarial de entrevistados que possuem nível Fundamental de ensino é: R${mediaFund:.2f}')
else:
  print('Nenhum entrevistado tem nível fundamental de ensino')

if totalMed > 0:
  mediaMed = (salMed / totalMed)
  print(f'A média salarial de entrevistados que possuem nível Médio de ensino é: R${mediaMed:.2f}')
else:
  print('Nenhum entrevistado tem nível médio de ensino')

if totalSup > 0:
  mediaSup = (salSup / totalSup)
  print(f'A média salarial de entrevistados que possuem nível Superior de ensino é: R${mediaSup:.2f}')
else:
  print('Nenhum entrevistado tem nível superior de ensino')


