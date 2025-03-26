num = 0
somaPar = 0
somaImpar = 0

for num in range(10, 100):
  if (num % 2 == 0):
    somaPar += num

  else:
    somaImpar += num

print(f"A soma dos números Pares é: {somaPar}")
print(f"A soma dos números Ímpares é: {somaImpar}")
