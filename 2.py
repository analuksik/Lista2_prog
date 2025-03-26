contador = 0
soma = 0
qtd = 0

print(f"Os múltiplos de 11 no intervalo [200, 100] são: ")

for contador in range(200, 99, -1):
  if (contador % 11 == 0):
    print(f"{contador}")
    soma += contador
    qtd += 1

if qtd > 0:
    
  media = soma / qtd
  print(f"A soma dos múltiplos de 11 é: {soma}")
  print(f"A média dos múltiplos de 11 é: {media:.2f}")  
