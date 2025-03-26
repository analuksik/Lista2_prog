print('MENU: CADASTRO DE SEXO')
print('OPÇÃO [1]: HOMEM')
print('OPÇÃO [2]: MULHER\n')

contador, qtd_masc, qtd_fem = 0, 0, 0
maiorMasc, maiorFem = 0, 0
soma_hMasc, soma_hFem = 0, 0
mascG, femG = 0, 0
mediaH, mediaM, porcF, porcH = 0, 0, 0, 0

while contador < 4:

  try:
    sexo = int(input('Digite a opção referente ao seu sexo: '))

    if sexo != 1 and sexo != 2:
      print('Digite uma opção válida! ')
      print()
      continue

    h = float(input('Digite sua altura (m): '))
    print()

    if sexo == 1: 

      if h > maiorMasc: 
        maiorMasc = h #atualiza a altura do maior homem

      soma_hMasc += h #soma as alturas
      qtd_masc += 1 #soma a qtd de homens 

      if h > 1.82:
        mascG += 1 #qtd de homens maiores que 1.82

    elif sexo == 2:
      if h > maiorFem: 
        maiorFem = h #reserva a altura da maior mulher

      soma_hFem += h #soma as alturas 
      qtd_fem += 1 #soma a qtd de mulheres

      if h > 1.82:
        femG += 1 #mulheres que tem mais de 1.82

    contador += 1

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

if qtd_masc > 0:  

    porcH = (mascG / qtd_masc) * 100 #porcentagem de homens maiores que 1.82
    mediaH = soma_hMasc / qtd_masc #media da altura dos homens    


if qtd_fem > 0:
  porcF = (femG / qtd_fem) * 100 #porcentagem de mulheres maiores que 1.82
  mediaM = soma_hFem / qtd_fem #media da altura das mulheres

print(f'A altura da mulher mais alta é: {maiorFem:.2f} m')
print(f'A altura do homem mais alto é: {maiorMasc:.2f} m')
print(f'A média de altura entre as mulheres é: {mediaM:.2f}')
print(f'A média de altura entre os homens é: {mediaH:.2f}')
print(f'A porcentagem de mulheres maiores que 1.82 é: {porcF:.2f}%')
print(f'A porcentagem de homens maiores que 1.82 é: {porcH:.2f}%')
