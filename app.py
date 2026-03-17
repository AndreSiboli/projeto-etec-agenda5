device = input('Nome do aparelho? ')
watts = float(input('Qual a potência em watts? '))
average_usage_in_hour = float(input('Qual o tempo médio de uso diário em horas? '))

month_usage = (watts * average_usage_in_hour * 30) / 1000

price_per_kwh = 0.75
estimated_cost = month_usage * price_per_kwh

print(f'Aparelho: {device}')
print(f'Consumo estimado: {month_usage:.2f} kWh/mês')
print(f'Custo estimado: R$ {estimated_cost:.2f}')