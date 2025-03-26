try: 

  contador = 0

  for contador in range(3,101):
    if (contador % 3 == 0):
      print(f" {contador}")
      
except Exception as ERRO_EXCEÇÃO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXCEÇÃO}")
