try:

  limite_superior = int(input("Digite o limite superior: "))
  limite_inferior = int(input("Digite o limite inferior: "))
  n = int(input("Digite o valor de n: "))

  if n < 2:
      print("Valor inválido! n deve ser >= 2")

  elif limite_inferior < 0 or limite_superior < 0:
    print("Valor inválido! Os limites devemser números positivos! ")

  elif limite_superior < limite_inferior:
    print("Valor inválido! o Limite Superior deve ser maior do que o Limite Inferior!")

  else:  
    print(f"Os múltiplos de {n} no intervalo [{limite_inferior}, {limite_superior}] são: ")

  for i in range(limite_inferior,limite_superior):
    if i % n == 0:
      print(f"{i}")
      
except Exception as ERRO_EXCECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")      
