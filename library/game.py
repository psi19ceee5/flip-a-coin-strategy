import random
from library import player as ply

class Game :

    def __init__(self) :
        random.seed(0)

    def initialize(self, uplayer) :
        self.player = uplayer
        self.rounds = 0
        self.round_of_max_capital = 0
        self.init_stake = 1
        self.max_stake = self.init_stake
        self.stake = self.init_stake

    def set_init_stake(self, uinit_stake) :
        self.init_stake = uinit_stake
        self.stake = self.init_stake

    def set_random_seed(self, useed) :
        random.seed(useed)

    def is_on(self) :
        if self.player.get_capital() - self.stake >= 0 :
            return 1
        else :
            return 0
        
    def next_round(self) :
        success = bool(random.randint(0,1))
        if success :
            is_max_capital = self.player.update_capital(self.player.capital + self.stake)
            self.stake = self.init_stake
        else :
            is_max_capital = self.player.update_capital(self.player.capital - self.stake)
            self.stake = 2*self.stake
            if self.stake > self.max_stake :
                self.max_stake = self.stake
        if is_max_capital :
            self.round_of_max_capital = self.rounds
        
        self.rounds = self.rounds + 1

    def get_no_rounds(self) :
        return self.rounds

    def get_round_of_max_capital(self) :
        return self.round_of_max_capital

    def get_stake(self) :
        return self.stake

    def get_init_stake(self) :
        return self.init_stake
