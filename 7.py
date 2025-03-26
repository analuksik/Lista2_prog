i = 0
cont = 0
n = 0

for i in range(9, 98):
  if (i % 2 != 0) and (i % 3 == 0) and (i % 5 != 0):
    n += 1
    print(f"{n}° número: {i}")
    cont += i
  print(f"A soma dos números é: {cont}")
