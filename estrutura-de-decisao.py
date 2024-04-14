tempo_fumado = int(input("Quantos anos você fuma: "))
valor = float(input("Valor atual do maço: "))
quantidade_por_dia = int(input("Quantidade média de maços fumados por dia: "))

dias_fumando = tempo_fumado * 365
total_fumados = dias_fumando * quantidade_por_dia
total_gastos = total_fumados * valor

limite_inferior = 20000
limite_superior = 50000

print(f"Você fumou {total_fumados} cigarros ao longo de {dias_fumando} dias.")

if total_gastos <= limite_inferior:
    mensagem = "dar entrada em um carro"
elif limite_inferior < total_gastos <= limite_superior:
    mensagem = "comprar um carro popular usado"
else:
    mensagem = "comprar um carro zero"

print(f"Com o valor de R${total_gastos:.2f}, você poderia ter {mensagem}.")
