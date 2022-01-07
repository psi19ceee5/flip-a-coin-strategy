class Player :

    def __init__(self) :
        self.init_capital = 0
        self.capital = self.init_capital
        self.max_capital = self.init_capital

    def set_init_capital(self, uinit_capital) :
        self.init_capital = uinit_capital
        self.capital = self.init_capital
        self.max_capital = self.init_capital

    # returns wether a new maximum capital is reached
    def update_capital(self, ucapital) :
        self.capital = ucapital
        if self.capital > self.max_capital :
            self.max_capital = self.capital
            return True
        else :
            return False
        
    def get_capital(self) :
        return self.capital

    def get_init_capital(self) :
        return self.init_capital

    def get_max_capital(self) :
        return self.max_capital
