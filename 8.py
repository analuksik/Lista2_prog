op1 = 0
op2 = 0
op3 = 0
cliente = 0

while True:

  try:

    print("Qual sabor de mix você mais gostou?")
    opcao = int(input("Opções: 1: Mix 1, 2: Mix 2 ou 3: Mix 3"))
    print("Digite 0 para sair do progama")

    if opcao == 1:
      op1 += 1
    elif opcao == 2:
     op2 += 1
    elif opcao == 3:
     op3 += 1
    elif opcao == 0:
     break
    cliente += 1
  
  except Exception as ERRO_EXCECAO:
    print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")

if cliente > 0:  
  porc1 = (op1 / cliente) * 100
  porc2 = (op2 / cliente) * 100
  porc3 = (op3 / cliente) * 100

print(f"A porcentagem de clientes que preferem o mix 1 é de: {porc1:.2f}%")
print(f"Mix 2: {porc2:.2f}%")
print(f"Mix 3:{porc3:.2f}%")
