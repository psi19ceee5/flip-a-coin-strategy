from library import player as ply
from library import game as gm
from matplotlib import pyplot as plt
import numpy as np

def main() :

    player = ply.Player()
    game = gm.Game()
    game.set_random_seed(0)
    
    rounds = []
    maxcap = []

    ngames = 10000
    confidence = 0.95
    for i in range(ngames) :
        player.set_init_capital(5000)
        game.initialize(player)
        game.set_init_stake(1)

        while game.is_on() :
            game.next_round()

        rounds.append(np.log10(game.get_no_rounds()))
        maxcap.append(np.log10(player.get_max_capital()))

    plt.hist(rounds,bins=100,histtype='step')
    plt.yscale('log')
    plt.title("start capital: "+str(player.get_init_capital())+", stake: "+str(game.get_init_stake()))
    plt.xlabel('log10(rounds)')
    plt.ylabel('Entries')
    plt.savefig("rounds.pdf")

    plt.clf()
    
    plt.hist(maxcap,bins=100,histtype='step')
    plt.yscale('log')
    plt.title("start capital: "+str(player.get_init_capital())+", stake: "+str(game.get_init_stake()))
    plt.xlabel('log10(max. capital)')
    plt.ylabel('Entries')
    plt.savefig("maxcap.pdf")

    maxcap.sort()
    quantile = 10**maxcap[round((1 - confidence)*ngames)]
    print("Init capital:", player.get_init_capital(), "-> max. capital is increased to", 100*quantile/player.get_init_capital(), "% in", round(100*confidence), "% of all games")
    

if __name__ == "__main__" :
    main()
