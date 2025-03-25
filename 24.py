cont = 0

while cont < 2:
  try:

    preco = float(input(f'Digite o preço da {cont + 1}º mercadoria (R$): '))

    reaj = preco * 1.05

    if reaj > 25.50:
      reaj *= 0.98
     

    print(f'Com o reajuste, a {cont + 1} mercadoria vai custar: R${reaj:.2f}')  

    cont += 1

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
