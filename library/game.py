import random
from library import player as ply

class Game :

    def __init__(self) :
        self.initial_stake = 1

    def initialize(self, uplayer) :
        self.player = uplayer
        self.no_rounds = 0
        self.stake = self.initial_stake
        random.seed(0)

    def set_init_stake(self, uinit_stake) :
        self.initial_stake = uinit_stake
        self.stake = self.initial_stake

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
            print("   stake:", self.stake, " ...win")
            self.player.update_capital(self.player.capital + self.stake)
            self.stake = self.initial_stake
        else :
            print("   stake:", self.stake, "...loss")
            self.player.update_capital(self.player.capital - self.stake)
            self.stake = 2*self.stake
        
        self.no_rounds = self.no_rounds + 1

    def get_no_rounds(self) :
        return self.no_rounds

    def get_stake(self) :
        return self.stake
