print('MENU: CADASTRO DE VOTOS ')
print('OPÇÃO [1]: CANDIDATO 1')
print('OPÇÃO [2]: CANDIDATO 2')
print('OPÇÃO [0]: VOTO NULO')

eleitor, cand1, cand2, nulo = 0, 0, 0, 0
porc1, porc2, porcNulo, totalVoto = 0, 0, 0, 0

while eleitor < 6:
  try:

    opcao = int(input('DIGITE A SUA OPÇÃO DE VOTO: '))
    if opcao == 1:
      cand1 += 1

    elif opcao == 2:
      cand2 += 1

    elif opcao == 0:
      nulo += 1

    else:
      print('OPÇÃO DE VOTO INVÁLIDA!')
      print('ESCOLHA ENTRE AS OPÇÕES LISTADAS.')
    eleitor += 1
    totalVoto = cand1 + cand2 + nulo

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    2
porc1 = (cand1 / totalVoto) * 100
porc2 = (cand2 / totalVoto) * 100
porcNulo = (nulo / totalVoto) * 100
print(f'A porcentagem de votos no candidato 1 é: {porc1:.2f}%')
print(f'A porcentagem de votos no candidato 2 é: {porc2:.2f}%')
print(f'A porcentagem de votos nulos é: {porcNulo:.2f}%')    
