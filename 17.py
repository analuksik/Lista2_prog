menor = None

while True:

  try:

    num = float(input("Digite um número inteiro positivo: "))
  
    if num == 0:
      break

    elif num < 0:
      print('Digite apenas números positivos!')  
    
    elif menor is None or num < menor:
      menor = num

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')    
print(f'O menor número digitado foi: {menor}')  
