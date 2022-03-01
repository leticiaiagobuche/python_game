from random import randint

class cliente:
    def __init__(self):
        self.dinheiro = randint(0,100)
        self.cesta = 30
        print(f'\nO cliente começou com {self.dinheiro} reais.\n')