soma = 0
qtd = 0

try:
    x = int(input("Digite o valor de x: "))
    if x < 1:
        print("ERRO DADOS DE ENTRADA: x DEVE SER >= 1")
        exit()
    
    for i in range(6, 6 * x + 1, 6):  # Agora inclui 6 * x
        soma += i
        qtd += 1  

    media = soma / qtd  # Média calculada corretamente
    print(f"A média dos múltiplos de 6 no intervalo [6, {6 * x}] é: {media:.2f}.")
    
except ValueError:
    print("ERRO: Entrada inválida! Digite um número inteiro.")
