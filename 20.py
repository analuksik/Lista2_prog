print('MENU: CADASTRO DE CLIENTES ')
print('OPÇÃO [1]: CADASTRAR CLIENTE ')
print('OPÇÃO [0]: SAIR DO PROGRAMA \n')

vip, stand, total = 0, 0, 0
porcVip, porcStand = 0, 0

while True:
  try:

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
      salario = float(input("Digite o valor do seu salário (R$): "))
      if salario >= 1500:
        vip += 1
      else:
        stand += 1

      total +=1

    elif opcao == 0:
      break
    
    else:
      print('DIGITE UMA OPÇÃO VÁLIDA. ')

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXECAO}')  

porcVip = (vip / total) * 100
porcStand = (stand / total) * 100
print(f'De {total} clientes, {porcVip}% são cadastrados no cartão VIP')
print(f'E {porcStand}% são cadastrados no cartão STANDART')
