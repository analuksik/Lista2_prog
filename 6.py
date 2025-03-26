cliente = 0
A = 0
B = 0
C = 0
SM = 998.05

while (cliente < 3):

  try:

    salario = float(input("Digite o seu salário em reais (R$): "))
    cliente += 1
    if salario >= (SM * 15):
      A += 1
    elif salario >= (SM * 5):
      B += 1
    else:
      C += 1
 
  except Exception as ERRO_EXCECAO:
    print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")

porc_A = (A / cliente) * 100
porc_B = (B / cliente) * 100
porc_C = (C / cliente) * 100 
print(f"A porcentagem de clientes do tipo A é: {porc_A:.2f}%")
print(f"A porcentagem de clientes do tipo B é: {porc_B:.2f}%")
print(f"A porcentagem de clientes do tipo C é: {porc_C:.2f}%")   
