class Player :

    def __init__(self) :
        self.init_capital = 0
        self.capital = 0

    def set_init_capital(self, uinit_capital) :
        self.init_capital = uinit_capital
        self.capital = self.init_capital

    def update_capital(self, ucapital) :
        self.capital = ucapital

    def get_capital(self) :
        return self.capital
        

