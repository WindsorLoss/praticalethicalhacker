from Sapatos import Sapatos

low = Sapatos('And 1s', 30)
medium = Sapatos('Air Force 1s', 120)
high = Sapatos('Off Whites', 400)

shoes = [high, medium, low]

try:
    shoe_budget = float(input('Qual é o seu orçamento? '))
except ValueError:
    exit('Valor inválido. Insira um número!')

for shoe in shoes:
    shoe.buy(shoe_budget)