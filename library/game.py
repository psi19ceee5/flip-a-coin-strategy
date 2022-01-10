import random
from library import player as ply

class Game :

    def __init__(self) :
        random.seed(0)

    def initialize(self, uplayer) :
        self._player = uplayer
        self._rounds = 0
        self._round_of_max_capital = 0
        self._reset_initial_stake()
        self._max_stake = self._init_stake
        self._stake = self._init_stake

    def set_random_seed(self, useed) :
        random.seed(useed)

    def is_on(self) :
        if self._player.capital - self._stake >= 0 :
            return 1
        else :
            return 0
        
    def next_round(self) :
        success = bool(random.randint(0,1))
        if success :
            is_max_capital = self._player.update_capital(self._player.capital + self._stake)
            self._adjust_stake_success()
        else :
            is_max_capital = self._player.update_capital(self._player.capital - self._stake)
            self._adjust_stake_loss()
            if self._stake > self._max_stake :
                self._max_stake = self._stake
        if is_max_capital :
            self._round_of_max_capital = self._rounds
        
        self._rounds = self._rounds + 1

    # argumants: "initial stake", parameter = <initial stake>
    #            "rise relative to capital", parameter = <fraction>
    def set_strategy_success(self, ustrategy, uparam = 0) :
        self._sstrategy = ustrategy
        self._sparam = uparam

    # arguments: "double stake"
    def set_strategy_loss(self, ustrategy, uparam = 0) :
        self._lstrategy = ustrategy
        self._lparam = uparam

    def get_no_rounds(self) :
        return self._rounds

    def get_round_of_max_capital(self) :
        return self._round_of_max_capital

    def get_stake(self) :
        return self._stake

    def get_init_stake(self) :
        return self._init_stake

    # private:

    def _reset_initial_stake(self) :
        if self._sstrategy == 'initial stake' :
            if self._sparam <= 0 :
                raise Exception("Warning: Initial stake is <= 0. This might lead to an infinite game")
            self._init_stake = uparam
            self._stake = self._init_stake
            return
        if self._sstrategy ==  "rise relative to capital" :
            self._init_stake = self._sparam*self._player.capital
            return

    def _adjust_stake_success(self) :
        if self._sstrategy == "initial stake" :
            self._set_stake_to_initial()
            return
        if self._sstrategy == "rise relative to capital" :
            self._rise_rel_capital()
        else :
            pass

    def _adjust_stake_loss(self) :
        if self._lstrategy == "double stake" :
            self._double_stake()
            return
        else :
            pass

    def _set_stake_to_initial(self) :
        self._stake = self._init_stake

    def _double_stake(self) :
        self._stake = 2*self._stake

    def _rise_rel_capital(self) :
        self._stake = self._sparam*self._player.capital
        
