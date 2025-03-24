try: 
  empregado = 0
  desempregado = 0
  hab = 0
  while (hab < 10001):
    status = str(input(f"Você trabalha? (S/N): "))
    hab += 1
    if status == 'S':
      empregado += 1
    elif status == 'N':
      desempregado += 1 
  print(f"Número de habitantes empregados: {empregado}")
  print(f"Número de habitantes desempregados: {desempregado}")

  desemp_porc = (desempregado / hab) * 100
  emp_porc = (empregado / hab) * 100

  print(f"Porcentagem de habitantes empregados: {emp_porc}%")
  print(f"Porcentagem de habitantes deempregados: {desemp_porc}%")
except Exception as ERRO_EXCECAO:
  print(f"ERRO DE EXCEÇÃO:{ERRO_EXCECAO}")
