def calculadora(n1, n2, operacao):
  if operacao == 1:
    res = n1 + n2
  elif operacao == 2:
    res = n1 - n2
  elif operacao == 3:
    res = n1 * n2
  elif operacao == 4:
    res = n1 / n2
  else:
    res = 0
  return res

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))
res = calculadora(n1, n2, operacao)

print("O resultado é: ", res)
