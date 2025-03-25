menor = None
i, inscricao_venc = 0, 0

while i < 3:
  try:
    inscricao = int(input("Digite o número da sua inscrição: "))
    tempo = float(input('Qual foi o seu tempo de prova? (em minutos) '))

    if menor is None or tempo < menor:
      menor = tempo
      inscricao_venc = inscricao
    i += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    
print(f"O vencedor é o de inscrição número: {inscricao_venc}")
print(f"Com o tempo de prova: {menor} minutos") 
