class Sapatos:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def budget_check(self, budget):
        if not isinstance(budget, (int, float)): #Verifica se o argumento budget é um dos dois tipos
            print('Valor de orçamento inválido! Por favor insira um número!')
            exit()

    def change(self, budget):
        return (budget - self.price)

    def buy(self, budget):
        self.budget_check(budget)

        if budget >= self.price:
            print(f'\nVocê pode pegar, {self.name}')

            if budget == self.price:
                print('Você tem a quantidade exata para comprar esses sapatos')

            else:
                print(f'O seu troco é de: ${self.change(budget)}')

            exit('\nObrigado por usar o ShoeBudget App!!!')